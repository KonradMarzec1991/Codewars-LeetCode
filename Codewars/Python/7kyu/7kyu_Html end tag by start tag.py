def html_end_tag_by_start_tag(start_tag):
    import re
    return f"</{re.match(r'^<([a-z]+)', start_tag).group(1)}>"