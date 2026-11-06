"""Published "Not before" floor: no match starts before its earliest slot.

A locked match (called, playing, finished, hard-locked) is exempt and keeps
its slot. A hard pin below the floor is recorded as a named infeasibility
reason rather than left to surface as a generic INFEASIBLE. Must run after
``freeze_horizon``, which adds to ``locked_matches``.
"""
from __future__ import annotations

from scheduler_core.engine.constraints import (
    ConstraintContext,
    register_constraint,
)


@register_constraint
class EarliestStart:
    name = "earliest_start"

    def __init__(self) -> None:
        pass

    def apply(self, ctx: ConstraintContext) -> None:
        for match_id, match in ctx.matches.items():
            floor = match.earliest_slot
            if not floor or floor <= 0 or match_id in ctx.locked_matches:
                continue
            prev = ctx.previous_assignments.get(match_id)
            if prev is not None and prev.pinned_slot_id is not None and prev.pinned_slot_id < floor:
                ctx.infeasible_reasons.append(
                    f"Match {match.event_code}: pinned at slot {prev.pinned_slot_id}, "
                    f"before its published Not before (slot {floor})"
                )
                continue
            ctx.model.Add(ctx.svars.start[match_id] >= floor)
