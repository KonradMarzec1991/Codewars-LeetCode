def money_value(s):
    try:
        s = s.replace("$", "")
        s = s.replace(" ", "")
        return float(s)
    except:
        return 0.0
