# schedule-engine

CP-SAT tournament scheduler.

| Part | Files |
|---|---|
| Rules | `scheduler_core/domain/models.py` |
| Encoding | `scheduler_core/engine/constraints/` |
| Solver | `scheduler_core/engine/cpsat_backend.py` |
| Checker | `scheduler_core/engine/validation.py` |

```bash
pip install -e .
python examples/basic.py
```
