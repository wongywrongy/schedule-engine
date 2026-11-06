"""Scheduler core library: the pure CP-SAT scheduling layer.

Public API (stable, minimal):
- schedule(problem, *, options?) -> ScheduleResult

Core is usable without FastAPI and without importing app schemas.
"""
from scheduler_core.domain import (
    Assignment,
    Match,
    Player,
    PreviousAssignment,
    ScheduleConfig,
    ScheduleRequest,
    ScheduleResult,
    SoftViolation,
    SolverOptions,
    SolverStatus,
    FrameworkError,
    ValidationError,
    InfeasibleError,
)
from scheduler_core.schedule import schedule

# Backends (for extension and advanced usage)
from scheduler_core.engine import (
    CPSATBackend,
    CPSATScheduler,
    SchedulingBackend,
)
__all__ = [
    "schedule",
    "ScheduleRequest",
    "ScheduleResult",
    "ScheduleConfig",
    "SolverOptions",
    "SolverStatus",
    "Assignment",
    "Match",
    "Player",
    "PreviousAssignment",
    "SoftViolation",
    "FrameworkError",
    "ValidationError",
    "InfeasibleError",
    "CPSATScheduler",
    "CPSATBackend",
    "SchedulingBackend",
]
