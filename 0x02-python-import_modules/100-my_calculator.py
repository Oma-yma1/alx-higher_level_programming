#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        sys.exit(0)
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        sys.exit(0)
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        sys.exit(0)
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
