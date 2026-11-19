# Quick start

Use the [v1.0.0 schema](traveler-profile/1.0.0/schema.json) with a JSON Schema Draft 2020-12 validator. Set the profile's `schemaVersion` to `1.0.0`. The following commands run from the repository root with Python 3.11 or newer.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install 'jsonschema[format]>=4.18,<5'
python docs/traveler-profile/1.0.0/verify.py
```

The verifier prints the schema checksum, the checks it passed, the example hotel payload and the doorway graph record. [Download the expected results](traveler-profile/1.0.0/validation-results.json).

## Validate a profile

Begin with the [minimal profile](examples/minimal.json). It supplies the five required sections and an empty grants array. Replace the example path below to validate your own record. Format checking is explicit.

```python
import json
from pathlib import Path
from jsonschema import Draft202012Validator

root = Path("docs")
schema = json.loads((root / "traveler-profile/1.0.0/schema.json").read_text())
profile = json.loads((root / "examples/minimal.json").read_text())
validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
validator.validate(profile)
```

For a fuller integration fixture, use the [synthetic traveller](examples/traveller.json). Keep a local copy of the versioned schema in a validating service so that input validation can run offline. Run consent checks separately at the point of access or disclosure.
