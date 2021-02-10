def scoreboard(who_ate_what):
    for c in who_ate_what:
        score = 0
        if 'chickenwings' in c.keys():
            score += c.pop('chickenwings') * 5
        if 'hamburgers' in c.keys():
            score += c.pop('hamburgers') * 3
        if 'hotdogs' in c.keys():
            score += c.pop('hotdogs') * 2
        for k in list(c.keys()):
            if k != 'name':
                del c[k]
        c.update({'score': score})
    return sorted(who_ate_what, key=lambda x: (-x['score'], x['name']))