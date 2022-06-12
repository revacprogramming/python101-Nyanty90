# Lists

with open((fn := "./py-101/dataset/romeo.txt")) as f:
    l = [wrd for lne in f for wrd in lne.split()]
    ul = []
    for uwrd in l:
        if uwrd not in ul:
            ul.append(uwrd)  # list comprehension didnt work here for some reason and I didn't want to spend more time on it :(
    ul.sort()
    print(ul)
