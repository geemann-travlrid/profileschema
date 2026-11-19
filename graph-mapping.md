# Graph mapping

Use each field's `x-key` as its canonical identifier and `x-kind` to distinguish a fact, trip default, preference or requirement. Preserve facts and trip defaults in their original roles. Keep explicit context, provenance, unit and strength where supplied.

| Input | Interpretation |
| --- | --- |
| Strength +100 | The condition must hold. |
| Strength -100 | The condition must be avoided. |
| Strength 0 | Neutral. |
| Intermediate strength | Soft preference with the indicated direction and magnitude. |
| Measured limit without strength | Effective strength +100. Retain the original omission when reconstructing the profile. |
| Other unscored requirement | Mandatory requirement. |

For measurements, apply the field's `x-comparison` to the supplier value. Use inclusive comparison for `gte` and `lte` and equality for `eq`. Compare values in the declared unit.

## Doorway example

A traveller supplies a minimum doorway width of 0.85 m and omits strength. The graph retains the minimum operator, value and unit, with effective strength +100. A confirmed width of 0.85 m meets that threshold. A confirmed width of 0.84 m falls below it. An unknown width needs confirmation. When serialising back to the traveller profile, preserve the original omission of strength.

The [validation results](traveler-profile/1.0.0/validation-results.json) include the example graph record. The [field reference](field-reference.md) lists the keys available for mapping.
