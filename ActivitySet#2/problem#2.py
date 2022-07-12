def input_two_numbers():
    return (a := int(input("Num1 "))), (b := int(input("Num2 ")))


def add(a, b):
    return a + b


def output(a, b, s):
    print("{} + {} = {}".format(a, b, s))


def main():
    a, b = input_two_numbers()
    output(a, b, (s := add(a, b)))


if __name__ == '__main__':
    main()
