# Ciąg Fibonacciego iteracyjnie
def Fib(n):

    if not isinstance(n, int):
        return 'Must be int'

    if n == 0:
        return 0

    if n == 1:
        return 1

    k = 0
    l = 1

    final = 0

    for x in range(n - 1):
        final = k + l
        k = l
        l = final

    return final


# print(Fib(7))
# print(Fib(10))
# print(Fib(15))


#Ciąg Fibonnacciego rekurenycjnie
def Fib2(n):

    if not isinstance(n, int):
        return 'Must be int'

    if n < 0:
        return 'Impossible to run'

    if n == 0:
        return 0

    if n == 1:
        return 1

    return Fib2(n-1) + Fib2(n-2)


# print(Fib(7))
# print(Fib(10))
# print(Fib(15))

# Program do wczytywania liczb
def inp2(n):

    num = input('Write integer, please: ')

    try:
        num = int(num)
    except:
        return 'Not a number!'

    if n <= 0:
        return 'Positve number, please!'

    arr = []

    for x in range(1, n):
        arr.append(2 ** x)

    return arr


# print(inp2(5))


# Odczyt pliku i przekazanie
def read_file(file_input, file_output):

    f_arr = []
    m_arr = []

    result = ''

    output = open(file_output, 'w+')

    with open(file_input, 'r+') as f:
        for line in f:

            arr = line.split(",")

            if arr[3].strip(" ") == 'K':
                f_arr.append(int(arr[2]))

                if int(arr[4].strip('\n')) <= 150:
                    output.write(line)

                result += line

            elif arr[3].strip(" ") == 'M':
                m_arr.append(int(arr[2]))

                height = int(arr[4].strip("\n"))
                height += 1

                line = line.replace(arr[4], " " + str(height))

                result += line + '\n'
            
            else:
                result += line

    output.close()

    f = open(file_input, 'w')
    f.write(result)

    f.close()

    d = dict()

    d["f_avg"] = sum(f_arr)/len(f_arr)
    d['m_avg'] = sum(m_arr)/len(m_arr)
    d['sum_all'] = sum(f_arr) + sum(m_arr)

    return d


# print(read_file('file.txt', 'output.txt'))
