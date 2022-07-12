def add(a, b):
    return a + b


def main():
    c = add((a := int(input("Num1 "))), (b := int(input("Num2 "))))
    print(c)


if __name__ == '__main__':
    main()
