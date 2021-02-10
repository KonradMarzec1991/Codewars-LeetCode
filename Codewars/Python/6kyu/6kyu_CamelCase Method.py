def camel_case(string):
    if string == "":
        return ""
    s = string.strip(" ")
    return "".join(w.capitalize() for w in s.split())


