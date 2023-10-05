#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: {:s} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)

    operator = sys.argv[2]
    operators = {'+': add, '-': sub, '*': mul, '/': div}

    if operator not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = operators[operator](a, b)
    print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
