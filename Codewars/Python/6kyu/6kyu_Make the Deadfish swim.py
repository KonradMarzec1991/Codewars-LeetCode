def parse(data):
    initial, result = 0, []
    for command in data:
        if command == 'i':
            initial += 1
        elif command == 'd':
            initial -= 1
        elif command == 's':
            initial = initial ** 2
        elif command == 'o':
            result.append(initial)
    return result
