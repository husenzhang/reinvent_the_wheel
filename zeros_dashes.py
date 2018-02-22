
def remove_zeros_dashes(s):
    """
    remove non-trailing 0s and all - from a string 
    """
    pad = ['-', '0']
    keep = ''

    for char in s:
        if char not in pad:
            keep = keep + char
    return keep


