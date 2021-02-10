def get_strings(city):
    checked, output = [], []
    city = city.lower()
    for char in city:
        if char not in checked and char.isalpha():
            output.append(char + ':' + city.count(char) * '*')
            checked.append(char)
    return ','.join(output)