# entropy_rg.py

import numpy as np

def entropic_rg_flow(t, g0=0.5, rate=0.25):
    """
    Simulates RG flow under entropic scaling:
      g(t) = g0 / (1 + rate * t)
    Inputs:
      - t: array of RG time values
      - g0: initial coupling
      - rate: flow rate constant
    Returns:
      - array of g(t) values
    """
    return g0 / (1 + rate * t)

def beta_function(g, rate=0.25):
    """
    Computes beta function: β(g) = -rate * g^2
    """
    return -rate * g**2
