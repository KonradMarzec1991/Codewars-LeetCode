def letter_frequency(text):
    d, text = dict(), text.lower()
    for s in text:
        if s.isalpha():
            d[s] = d.get(s, 0) + 1
    t = list(d.items())
    return sorted(t, key=lambda k: (-k[1], k[0]))
