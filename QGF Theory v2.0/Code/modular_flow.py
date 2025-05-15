# modular_flow.py

import numpy as np

def apply_t_evolution(state_vector, t_diag):
    """
    Applies modular T-matrix evolution to a state vector.
    Inputs:
      - state_vector: numpy array of initial amplitudes
      - t_diag: numpy array of diagonal T entries (complex phases)
    Returns:
      - evolved_state: numpy array after T action
    """
    return t_diag * state_vector
