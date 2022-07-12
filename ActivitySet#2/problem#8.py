class Menu:
    def __init__(self):
        self.items = {}

    def __repr__(self):
        return '\n'.join(' '.join((item, str(price))) for item, price in self.items.items())+'\n'

    def __setitem__(self, item, price):
        self.items[item] = price


m = Menu()
m["idly"], m["vada"] = 10, 20
print(m)
