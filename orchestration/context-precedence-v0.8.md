# Context Precedence Protocol v0.8

Before routing Positioning, Creative, Copy, Media or CRO, resolve context using this authority order:

1. Current verified client context
2. Current campaign / performance data
3. Sourced evidence and Voice of Customer
4. Explicitly validated strategic decisions
5. Previous run memory
6. Inferences
7. Hypotheses

## Conflict rule
If two levels conflict, the higher-authority source wins unless it is demonstrably stale. The conflict must be logged.

## Memory rule
Memory is advisory, not authoritative. A previous run must never silently override current verified client context.

## Staleness
When context changes, conflicting lower-priority memory must be marked `superseded` rather than deleted.

## Gate
Positioning and Creative cannot become `ready` until material context conflicts are resolved.