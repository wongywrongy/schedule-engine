"""Scheduling backends (engines).

The CP-SAT backend consumes a ScheduleRequest and returns a ScheduleResult.
No format logic.
"""

from abc import ABC, abstractmethod
from typing import Optional

from scheduler_core.domain.models import (
    ScheduleRequest,
    ScheduleResult,
    SolverOptions,
)

from scheduler_core.engine.cpsat_backend import CPSATScheduler


class SchedulingBackend(ABC):
    """Backend that solves a scheduling request."""

    @abstractmethod
    def solve(self, request: ScheduleRequest) -> ScheduleResult:
        """Solve and return ScheduleResult."""
        ...


class CPSATBackend(SchedulingBackend):
    """CP-SAT backend. Uses existing CPSATScheduler."""

    def __init__(
        self,
        solver_options: Optional[SolverOptions] = None,
        candidate_pool_size: int = 0,
    ) -> None:
        self.solver_options = solver_options or SolverOptions()
        self.candidate_pool_size = candidate_pool_size

    def solve(self, request: ScheduleRequest) -> ScheduleResult:
        scheduler = CPSATScheduler(
            config=request.config,
            solver_options=request.solver_options or self.solver_options,
        )
        scheduler.add_players(request.players)
        scheduler.add_matches(request.matches)
        scheduler.set_previous_assignments(request.previous_assignments)
        scheduler.set_locked_assignments(request.locked_assignments)
        scheduler.build()
        return scheduler.solve(candidate_pool_size=self.candidate_pool_size)
