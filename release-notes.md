# Global Traveler Profile v1.0.0

First public edition, 19 November 2026. This release includes 524 annotated canonical keys, a common preference-strength scale, measured accessibility requirements and grants scoped by recipient, action, purpose and field. The source combines earlier Travlr ID profile work with fields drawn from the 17 November 2026 Focus Areas working draft. This is a Travlr ID publication. Fields marked `x-status: strawman` retain their provisional vocabulary status.

| Release file | Purpose |
| --- | --- |
| [Release package](traveler-profile/1.0.0/Global_Traveler_Profile_v1.0.0.zip) | Original distribution with schema, reference verifier and expected results. |
| [JSON Schema](traveler-profile/1.0.0/schema.json) | Machine-readable contract for version 1.0.0. |
| [Verifier](traveler-profile/1.0.0/verify.py) | Runs against the adjacent schema.json in this repository. |
| [Results](traveler-profile/1.0.0/validation-results.json) | 22 local checks and the expected hotel response. |

Schema SHA-256: `21108bbe56b8ea2c52da36d60f748f8a57705958cb8e650c32e38d53de79519a`.

The declared schema identifier is `https://schema.travlrid.com/traveler-profile/1.0.0/schema.json`. Use the downloadable schema above for offline resolution. Earlier profiles require explicit field mapping. Grants inherited without actions authorise no operations until reissued.
