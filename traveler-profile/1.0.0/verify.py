"""Run with Python 3 and jsonschema[format]. Local reference fixtures only."""
import hashlib
import json
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parent
schema_file = root / 'schema.json'
schema = json.loads(schema_file.read_text())
validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
profile = schema['examples'][0]
grant = profile['consentSettings']['grants'][0]
checks = []

def check(label, condition):
    if not condition:
        raise ValueError(label)
    checks.append(label)

Draft202012Validator.check_schema(schema)
check('Draft 2020-12 meta-schema', True)
check('All embedded profiles validate', all(validator.is_valid(p) for p in schema['examples']))
fields = {}
refs = set()
def index(node):
    if isinstance(node, dict):
        if 'x-key' in node:
            key = node['x-key']
            if key in fields:
                raise ValueError(key)
            fields[key] = node
        if '$ref' in node:
            refs.add(node['$ref'])
        for child in node.values():
            index(child)
    elif isinstance(node, list):
        for child in node:
            index(child)
index(schema)
check('524 distinct canonical keys', len(fields) == 524)
check('Internal references resolve', refs <= {'#/$defs/' + k for k in schema['$defs']})

def valid_grant(candidate):
    instance = deepcopy(profile)
    instance['consentSettings']['grants'] = [candidate]
    return validator.is_valid(instance)

for key in ('did', 'authorityRef'):
    copy = deepcopy(grant)
    del copy['grantedBy'][key]
    check('Guardian must supply ' + key, not valid_grant(copy))
copy = deepcopy(grant)
del copy['grantedBy']
check('Self grant may omit grantedBy', valid_grant(copy))
legacy = deepcopy(grant)
del legacy['actions']
check('Actionless grant rejected', not valid_grant(legacy))
check('Empty actions rejected', not valid_grant(dict(grant, actions=[])))

door, shower = grant['scope']
width = profile['accessibility']['arrivalEntryExit']['minEntryDoorWidth']
score = width.get('strength', 100)
graph = dict(key=door, comparison=fields[door]['x-comparison'], value=width['value'],
             unit=width['unit'], mustHonor=abs(score) == 100, effectiveStrength=score,
             strengthExplicit='strength' in width)
check('Doorway is an inclusive mandatory minimum', graph['comparison'] == 'gte'
      and graph['mustHonor'] and graph['effectiveStrength'] == 100)
restored = {k: graph[k] for k in ('value', 'unit')}
if graph['strengthExplicit']:
    restored['strength'] = graph['effectiveStrength']
check('Doorway round trip preserves supplied value and omitted strength', restored == width)

def instant(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))

# Evidence is a synthetic decision fixture for one named delegate and subject.
evidence = (profile['travelerIdentity']['did'], 'did:example:guardian',
            'urn:example:authority:guardian-001', 'parentOrGuardian')
def project(candidate, recipient=grant['granteeId'], purpose='accessibilityFulfilment',
            action='read', at='2026-11-20T10:00:00Z', authority=evidence, context=None):
    actor = candidate.get('grantedBy', {})
    moment = instant(at)
    if (not valid_grant(candidate) or recipient != candidate['granteeId']
            or action not in candidate.get('actions', []) or purpose not in candidate['purposes']
            or moment < instant(candidate['grantedAt'])
            or any(moment >= instant(candidate[k]) for k in ('revokedAt','expiresAt') if k in candidate)
            or ('contexts' in candidate and context not in candidate['contexts'])):
        return {}
    if actor.get('role','self') != 'self' and authority != (
            profile['travelerIdentity']['did'], actor['did'], actor['authorityRef'], actor['role']):
        return {}
    # The hotel requests three service fields. Only two fall within the grant.
    payload = {}
    for key in (door, shower, 'accessibility.medicalSupplies.minRefrigeratedVolume'):
        if any(key == scope or key.startswith(scope + '.') for scope in candidate['scope']):
            value = profile
            for part in key.split('.'):
                value = value[part]
            payload[key] = {k: value[k] for k in ('value','unit') if k in value} if isinstance(value,dict) else value
    return payload

expected = {door: {'value': 0.85, 'unit': 'm'}, shower: 100}
check('Exact hotel payload, excluding medical and authority records', project(grant) == expected)
for label, args in [('Wrong recipient', dict(recipient='other')), ('Wrong purpose', dict(purpose='marketing')),
                    ('Wrong action', dict(action='share')), ('Unverified delegate', dict(authority=None)),
                    ('Future grant', dict(at='2026-01-01T00:00:00Z')), ('At expiry',dict(at=grant['expiresAt']))]:
    check(label + ' denied', project(grant, **args) == {})
check('Legacy actionless grant denied', project(legacy) == {})
check('Revoked grant denied', project(dict(grant, revokedAt='2026-11-20T10:00:00Z')) == {})
check('Partial key segment denied', project(dict(grant, scope=['accessibility.bath'])) == {})
check('Whole segment prefix accepted', project(dict(grant, scope=['accessibility.bathroom'])) == {shower: 100})
print(json.dumps(dict(schemaSHA256=hashlib.sha256(schema_file.read_bytes()).hexdigest(),
                      passed=checks, hotelPayload=expected, doorwayGraphExample=graph), indent=2))
