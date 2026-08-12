# Constraint Classification Protocol v0.8.1

NEXUS must not treat every preference, historical behavior or previous decision as a permanent strategic prohibition.

## Classes
### HARD_CONSTRAINT
A current explicit requirement that must not be violated.
Examples: legal restriction, budget ceiling, explicit user prohibition, unavailable capability.

### SOFT_PREFERENCE
A current preference that should influence recommendations but may be challenged when evidence or strategic fit justifies an alternative.

### HISTORICAL_CHOICE
A previous behavior or decision. It is context, not a present instruction.

### CURRENT_HYPOTHESIS
A working assumption that must be tested or validated.

## Required fields
- statement
- class
- source
- verified_at
- scope
- rationale
- can_be_challenged
- review_trigger

## Strategic Fit interaction
`REJECTED` requires a HARD_CONSTRAINT or sufficiently strong current evidence of poor strategic fit. A SOFT_PREFERENCE alone should normally produce `SUPPORTING`, `EXPERIMENTAL`, or a recommendation with an explicit trade-off rather than automatic rejection.

## Memory rule
Historical choices must never be silently promoted to hard constraints by repetition across runs.