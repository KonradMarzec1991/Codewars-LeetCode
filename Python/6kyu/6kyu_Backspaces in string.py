def clean_string(s):
    from collections import deque
    stack = deque()
    for ch in s:
        if ch != '#':
            stack.append(ch)
        else:
            if len(stack) > 0:
                stack.pop()
    return ''.join(stack)