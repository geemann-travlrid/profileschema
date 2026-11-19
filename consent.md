# Consent and hotel fulfilment

A hotel wants to check doorway width, shower access and refrigerated storage. In the [synthetic profile](examples/traveller.json), the guardian grants the example hotel group permission to read the doorway and shower fields for accessibility fulfilment. The example decision takes place on 20 November 2026, inside the grant's validity period.

## Evaluate the request

1. Identify the traveller, requesting organisation or agent, intended action, purpose, context and requested canonical keys.
2. For each field, find a single grant that satisfies every condition. A scope may match an exact key or a prefix ending at a dotted segment boundary. A grant for `accessibility.bath` cannot match `accessibility.bathroom`.
3. Check the grant is active at the decision time. The start time is inclusive. Expiry and revocation take effect at their timestamps. Missing or empty actions confer no permission.
4. For a guardian or legal representative, resolve the internal authority reference and verify current authority for this traveller and operation. A role and an identifier alone cannot establish that relationship.
5. Return only the requested, authorised fulfilment values. Keep delegation evidence and internal notes out of the supplier response.

## Example response

```json
{
  "accessibility.arrivalEntryExit.minEntryDoorWidth": {"value": 0.85, "unit": "m"},
  "accessibility.bathroom.rollInShower": 100
}
```

[Download the expected payload](examples/hotel-payload.json). This is a worked projection using dotted keys. The reference verifier uses a synthetic authority decision and a fixed request. Production implementations need their own requester authentication, grant store, delegation verification and enforcement. A separate onward disclosure requires the corresponding authority for the share operation.
