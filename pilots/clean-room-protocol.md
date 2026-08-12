# Clean-room Pilot Protocol

## Why
A valid A/B comparison between orchestrator versions requires a fresh execution context. Reusing the same Cowork conversation contaminates the result with prior outputs, files, task state and memory.

## Rule
For every version comparison:
1. start a new Cowork conversation;
2. verify only the intended skill version is enabled/selected;
3. do not attach prior pilot outputs unless the test explicitly measures memory reuse;
4. paste exactly the same mission prompt;
5. do not correct Claude during the first run;
6. save the full response before any follow-up;
7. score with the canonical NEXUS Delivery Scorecard /100;
8. compare KEEP / FIX / REMOVE / ADD.

## Contamination signals
A run is invalid for cold-start comparison if Cowork says or implies:
- the mission has already been run;
- prior deliverables already exist;
- it is reusing previous task state;
- it skips steps because of context from the earlier run.

## Pilot modes
### Cold-start mode
Purpose: test orchestration quality from zero context.

### Memory mode
Purpose: test whether NEXUS reuses prior learnings correctly.

Never mix the two in the same benchmark.
