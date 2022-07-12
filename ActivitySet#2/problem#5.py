def get_cs():
    return input("Enter connect string: ")


def cs_to_dict(cs):
    d = {}
    for pair in cs.split(','):
        key, value = pair.split('=')
        d[key] = value
    return d


def dict_to_cs(d):
    cs = ''
    for key, value in d.items():
        cs += (key + '=' + value + ',')
    return cs[:-1]


def main():
    cs = get_cs()
    print((d := cs_to_dict(cs)))
    print((ccs := dict_to_cs(d)))


if __name__ == '__main__':
    main()
