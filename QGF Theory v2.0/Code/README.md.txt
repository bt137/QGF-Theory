# qgf-sim

Python simulation modules for the Quantum Geometric Framework (QGF) theory.

These files are imported by the Jupyter notebooks in `/notebooks/` and contain all computational logic for modular flow, fusion dynamics, entropic renormalization, and Yukawa path estimation.

## Modules

- `fusion.py`: Fusion rule lookup engine
- `modular_flow.py`: Modular T-matrix evolution
- `entropy_rg.py`: RG flow and beta function modeling
- `yukawa.py`: Yukawa suppression weights via quantum dimensions
- `tensor_utils.py`: F-symbol lookup for associativity checks

Each file is self-contained and can be imported directly.

## Usage Example

```python
from fusion import fusion_result
from entropy_rg import entropic_rg_flow
