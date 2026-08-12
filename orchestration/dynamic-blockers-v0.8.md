# Dynamic Blocker Protocol v0.8

Missing information must block only dependent decisions or deliverables.

## Unknown schema
Each unknown must declare:
- `id`
- `question`
- `status`: blocking | assumable | informational | resolved
- `blocks`: explicit list of stages/deliverables
- `safe_to_assume`: yes | no
- `assumption_if_used`
- `owner`

## Rule
Never say `mission blocked` when only a subset of outputs is blocked.

Example: missing price may block final offer economics or final conversion copy, while not blocking market research, angle exploration or a draft test architecture.

After every new source is loaded, requalify all existing blockers. Do not inherit blocker status blindly from previous runs.