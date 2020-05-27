def sum_of_a_beach(beach):
    import re
    return len(re.findall(r'Sand|Water|Fish|Sun', beach, re.IGNORECASE))