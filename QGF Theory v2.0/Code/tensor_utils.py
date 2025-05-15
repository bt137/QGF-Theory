# tensor_utils.py

def get_f_symbol(f_data, a, b, c, d, e):
    """
    Retrieve F-symbol from a DataFrame.
    Inputs:
      - f_data: DataFrame of F-symbols with columns ['a', 'b', 'c', 'd', 'e', 'F']
      - a, b, c, d, e: fusion labels
    Returns:
      - float value of F-symbol if found, else None
    """
    try:
        match = f_data[
            (f_data['a'] == a) &
            (f_data['b'] == b) &
            (f_data['c'] == c) &
            (f_data['d'] == d) &
            (f_data['e'] == e)
        ]
        return float(match['F'].values[0])
    except:
        return None
