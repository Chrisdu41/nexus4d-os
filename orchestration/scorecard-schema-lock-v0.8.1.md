# Scorecard Schema Lock v0.8.1

The NEXUS Delivery Scorecard has exactly ten immutable dimensions, each scored from 0 to 10:

1. Video / Execution
2. Marketing
3. AI leverage
4. Neuromarketing
5. Clarity
6. Differentiation
7. Evidence
8. Conversion
9. Feasibility
10. Testability

## Invariants
- Dimension names and weights are immutable in the canonical scorecard.
- Total = arithmetic sum of the ten dimensions, maximum 100.
- `Launch readiness`, `integrity`, `strategic fit`, or any mission-specific metric may be reported separately, but MUST NOT replace, rename, regroup, or reweight canonical dimensions.
- The score is a QA heuristic, never a prediction of sales, CPA, CPL, ROAS or business success.
- Every displayed total MUST include the ten component scores so the arithmetic is auditable.

## Failure condition
If the system cannot score one dimension responsibly, return `N/A` for that dimension and state that a canonical total cannot yet be computed. Never fabricate a substitute weighting.