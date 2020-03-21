def generate_hashtag(s):
    arr = '#' + ''.join([x.capitalize() for x in s.strip().split(' ')])
    return arr if 1 < len(arr) <= 140 else False
