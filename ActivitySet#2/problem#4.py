def get_cs():
    return input("Enter connected string: ")


def cs_to_lot(cs):
    return cs.split("-")


def lot_to_cs(lot):
    cs = str(lot[0])
    for i in range(1, len(lot)):
        cs += ('-' + lot[i])
    return cs


def main():
    cs = get_cs()
    print((lot := cs_to_lot(cs)))
    print((cs := lot_to_cs(lot)))


if __name__ == '__main__':
    main()
