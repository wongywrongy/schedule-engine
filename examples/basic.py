"""Basic core usage: ScheduleRequest -> schedule() -> ScheduleResult.

Run from project root:
  python examples/basic.py

No FastAPI or app schemas required.
"""
from scheduler_core import (
    schedule,
    ScheduleRequest,
    ScheduleConfig,
    Player,
    Match,
    SolverOptions,
)

# Build a minimal problem (core types only)
config = ScheduleConfig(total_slots=10, court_count=2)
players = [
    Player(id="p1", name="Alice"),
    Player(id="p2", name="Bob"),
]
matches = [
    Match(id="m1", event_code="MS-1", side_a=["p1"], side_b=["p2"]),
]
problem = ScheduleRequest(
    config=config,
    players=players,
    matches=matches,
    solver_options=SolverOptions(time_limit_seconds=5.0),
)

# Single entry point
result = schedule(problem, options=problem.solver_options)

print(f"Status: {result.status.value}")
for a in result.assignments:
    print(f"  {a.match_id} -> slot {a.slot_id}, court {a.court_id}")
