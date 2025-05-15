# yukawa.py

def estimate_path_weight(objects, quantum_dims):
    """
    Estimate categorical suppression weight for a fusion path.
    Inputs:
      - objects: list of object labels (as strings)
      - quantum_dims: dictionary mapping label → dimension
    Returns:
      - inverse product of quantum dimensions
    """
    weight = 1.0
    for obj in objects:
        label = str(obj).strip()
        dim = quantum_dims.get(label, 1)
        weight *= dim
    return 1 / weight if weight != 0 else 0
