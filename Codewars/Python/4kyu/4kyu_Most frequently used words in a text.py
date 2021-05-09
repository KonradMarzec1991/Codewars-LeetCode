import re
from collections import Counter


def top_3_words(text):
    counter = Counter(re.findall(r'\'*[a-z][a-z|\']*', text.lower()))
    return [item[0] for item in counter.most_common(3)]
