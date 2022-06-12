# Loops & Iterators

l, s = None, None
while True:
    n = input("Enter num ")
    if n == "done":
        break
    try:
        n = int(n)
    except:
        print("Invalid input")
        continue
    if l is None:
        l = n
    elif n > l:
        l = n
    if s is None:
        s = n
    elif n < s:
        s = n
    print(n)

print("Maximum", l)
print("Minimum", s)
