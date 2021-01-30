import re


def is_a_valid_message(message):
    if not message:
        return True
    if message[0].isalpha():
        return False
    sub, num, char = [], '', ''
    for c in message:
        if c.isdigit():
            if char:
                sub.append(char)
                char = ''
            num += c
        else:
            if num:
                sub.append(int(num))
                num = ''
            char += c
    if char:
        sub.append(char)
    if num:
        sub.append(num)
    if len(sub) % 2 != 0:
        return False
    return all(sub[i] == len(sub[i+1]) for i in range(0, len(sub), 2))


# Great CW solution
def is_a_valid_message_2(message):
    return all(
        int(m.group(1) or 0) == len(m.group(2))
        for m in re.finditer(r'(\d*)([a-zA-Z]*)', message)
    )