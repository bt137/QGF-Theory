# fusion.py

def fusion_result(a, b, rules_dict):
    """
    Return the fusion result of objects a and b using a dictionary of fusion rules.
    Example format of rules_dict: {("1/2", "1/2"): "0 ⊕ 1"}
    """
    key = (a.strip(), b.strip())
    return rules_dict.get(key, f"No fusion rule for ({a}, {b})")
