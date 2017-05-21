
def mul(a, b):
    return a*b

def add(a, b):
    return a+b

def div(a, b):
    return a/b

def sub(a, b):
    return a-b

digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
decimal = '.'
operators = {'*' : mul,
             '+' : add,
             '/' : div,
             '-' : sub}

paran = {'open': '(',
         'close': ')'}

def calculate(data):
    num_stack, opr_stack = parse(data)

    while opr_stack:
        opr = opr_stack.pop()
        num1 = num_stack.pop()
        num2 = num_stack.pop()
        res = opr(num1, num2)
        num_stack.append(res)
    return num_stack[0]

def parse(data):
    num_stack = []
    opr_stack = []
    a = ''
    for d in data:
        if d in digits:
            a = a + d
        if d in operators:
            opr_stack.append(operators[d])
            num_stack.append(float(a))
            a = ''

    num_stack.append(float(a))
    return num_stack, opr_stack

'''
while True:
    result = calculate(input())
    print(result)

'''