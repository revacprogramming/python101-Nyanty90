class Menu:
    def __init__(self):
        self.items = {}

    def __repr__(self):
        return '\n'.join(' '.join((item, str(price))) for item, price in self.items.items())+'\n'

    def __add__(self, item):
        self.items[item[0]] = item[1]
        return self


m = Menu()
m = m + ("idly", 10) + ("vada", 20)
print(m)
