factorial_list = [1]


def check_input(n):
    return isinstance(n, int) and n > 0


def factorial(n):
    if n < len(factorial_list):
        return factorial_list[n]

    fact = factorial_list[-1]
    for i in range(len(factorial_list), n+1):
        fact *= i
        factorial_list.append(fact)
    return fact


def approx_sin(x, n):
    if not check_input(n):
        print('n must be an integer and greater than 0')
        return

    sin = 0
    for i in range(n):
        temp = 2*i + 1
        sin += (-1)**i * x**(temp) / factorial(temp)
    print(sin)


def approx_cos(x, n):
    if not check_input(n):
        print('n must be an integer and greater than 0')
        return

    cos = 0
    for i in range(n):
        temp = 2*i
        cos += (-1)**i * x**(temp) / factorial(temp)
    print(cos)


def approx_sinh(x, n):
    if not check_input(n):
        print('n must be an integer and greater than 0')
        return

    sinh = 0
    for i in range(n):
        temp = 2*i + 1
        sinh += x**(temp) / factorial(temp)
    print(sinh)


def approx_cosh(x, n):
    if not check_input(n):
        print('n must be an integer and greater than 0')
        return

    cosh = 0
    for i in range(n):
        temp = 2*i
        cosh += x**(temp) / factorial(temp)
    print(cosh)

