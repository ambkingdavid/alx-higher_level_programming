#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    op = {"+": "add", "-": "sub", "*": "mul", "/": "div"}
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        sn = sys.argv[2]
        if sn in op.keys():
            print("{} {} {} = {}".format(a, sn, b, op[sn](a, b)))
