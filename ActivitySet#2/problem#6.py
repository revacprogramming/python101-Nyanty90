class Menu:
    def __init__(self):  # name, items, start_time, end_time):
        self.items = {}

    def __repr__(self):
        return "\nMenu:\n{}\n".format(list((item, price) for item, price in self.items.items()))

    def add(self, item, price):
        self.items[item] = price

    def show(self):
        for item in self.items:
            print(item, self.items[item])


m = Menu()
m.add("idly", 10)
m.add("vada", 20)
m.show()
# print(repr(m))
