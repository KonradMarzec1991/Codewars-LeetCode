def domain_name(url):
    import re
    return re.match(r'^(http[s]?:\/\/)?([w]{3}\.)?([a-zA-Z0-9_-]+)', url).group(3)
