def get_cs():
    return input("Enter connected string: ")


def cs_to_lot(cs):
    return cs.split("-")


def main():
    cs = get_cs()
    print((lot := cs_to_lot(cs)))


if __name__ == '__main__':
    main()
