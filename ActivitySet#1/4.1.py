# Conditional Execution

h = float(input("Hrs "))
r = float(input("Rph "))
print(((40 * r) + ((h - 40) * (r * 1.5))) if h > 40 else (h * r))
