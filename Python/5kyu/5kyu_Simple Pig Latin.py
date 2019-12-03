import re


def pig_it(text):
    word_re = re.compile(r'\w+')

    def process_match(match):
        word = match.group()
        return word[1:] + word[0] + 'ay'

    new_text = word_re.sub(process_match, text)
    return new_text
