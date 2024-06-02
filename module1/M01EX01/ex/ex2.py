import math

alpha = 0.01

def is_number(x):
    try:
        float(x)
    
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1.0 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def elu(x, alpha=alpha):
    return x if x > 0 else alpha*(math.exp(x) - 1)


def activation_functions():
    x = input('Input x: ')
    if not is_number(x):
        print(f'{x} must be a number')
        return
    
    func_name = input('Input activation function: (sigmoid | relu | elu) : ')
    functions = {'sigmoid': sigmoid, 'relu': relu, 'elu': elu} 
    
    if func_name not in functions.keys():
        print(f'{func_name} is not supported')
        return
    
    res = functions[func_name](float(x))
    
    print(f'{func_name}({x}) = {res}')
    
    
def exercise2():
    activation_functions()