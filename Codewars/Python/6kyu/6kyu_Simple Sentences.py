def make_sentences(parts):
    output = '' + parts[0]
    for i in range(1, len(parts)):
        if parts[i] not in (',', '.', ' '):
            output = output + ' ' + parts[i]
        if parts[i] == ' ':
            continue
        if parts[i] == ',':
            output = output + ','
        if parts[i] == '.':
            output += parts[i]
            return output.strip()
    return output.strip() + '.'


# Amazing solution for CW
def make_sentences_v2(parts):
    return ' '.join(parts).replace(' ,', ',').strip(' .') + '.'

