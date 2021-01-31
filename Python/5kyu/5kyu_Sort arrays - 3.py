def sort_me(courses):
    return sorted(courses, key=lambda item: (int(item[-4:]), item[:-5]))
