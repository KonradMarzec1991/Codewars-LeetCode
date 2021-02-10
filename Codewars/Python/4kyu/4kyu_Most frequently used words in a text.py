import re
from collections import Counter


def top_3_words(text):
    counter = Counter(re.findall(r'\'*[a-z][a-z|\']*', text.lower()))
    return [item[0] for item in counter.most_common(3)]


print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))

print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))

print(top_3_words("  //wont won't won't"))