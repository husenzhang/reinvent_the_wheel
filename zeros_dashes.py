
def remove_zeros_dashes(s):
    """
    remove from string s:
    non-trailing 0s,  all '-', but keep trailing 0s
    """
    s = s.strip('-')
    num_tailing_zeros = len(s) - len(s.rstrip('0'))

    pad = ['-', '0', ' ']
    keep = ''

    for char in s:
        if char not in pad:
           keep = keep + char
    
    return keep + '0'*num_tailing_zeros


