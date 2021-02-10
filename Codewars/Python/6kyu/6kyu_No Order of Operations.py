def no_order(equation):
    import re
    equation = equation.replace(' ', '')
    numbers = re.findall(r'\d+', equation)
    signs = [e for e in equation if e in '+-*/^%']

    def get_sign(sign):
        if sign == '^':
            sign = '**'
        if sign == '/':
            sign = '//'
        return sign

    v1 = numbers.pop(0)
    while numbers:
        sign = get_sign(signs.pop(0))
        v_next = numbers.pop(0)
        try:
            v1 = eval(v1 + sign + v_next)
        except ZeroDivisionError:
            return None
        v1 = str(v1)
    return int(v1)


# Amazing solution from CW of Senior_Vadik, Rud1
def no_order_v2(equation):
    equation = equation.replace(' ', '')
    equation = equation.replace('+', ')+')
    equation = equation.replace('-', ')-')
    equation = equation.replace('*', ')*')
    equation = equation.replace('/', ')//')
    equation = equation.replace('%', ')%')
    equation = equation.replace('^', ')**')
    equation = '('*equation.count(')') + equation
    try:
        return eval(equation)
    except ZeroDivisionError:
        pass

