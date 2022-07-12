class Menu(dict):
    def __init__(self):
        self.items = {}

    def __repr__(self):
        return "\nMenu:\n{}\n".format(list((item, price) for item, price in self.items.items()))

    def __setitem__(self, item, price):
        self.items[item] = price
        return self


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items = {}

    def __repr__(self):
        return "\nOrder:\n{}\n".format(list((item, str(qty)) for item, qty in self.items.items()))

    def __setitem__(self, item, qty):
        self.items[item] = qty
        return self


class Bill:
    def __init__(self, menu, order):
        self.menu = menu
        self.order = order
        self.total = self.calc(self.menu, self.order)

    def __repr__(self):
        print("\nFollowing items are not available:")
        print(*(list(set(self.order.items.keys()) -
              set(self.menu.items.keys()))), sep=', ')
        return "\nTotal: {}\n".format(self.total)

    def calc(self, menu, order):
        total = 0
        for item, qty in order.items.items():
            if item in list(menu.items.keys()):
                total += menu.items[item] * qty
        return total


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2
    o["foo"] = 2
    o["bar"] = 2
except KeyError as e:
    print(e, 'err')

b = Bill(m, o)
print(b)
