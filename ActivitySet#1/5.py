# Functions

def computepay(h, r):
    return (40 * r) + ((h - 40) * (r * 1.5)) if h > 40 else (h * r)


hrs = float(input("Hrs "))
rph = float(input("Rph "))
print("Pay ", computepay(hrs, rph))
