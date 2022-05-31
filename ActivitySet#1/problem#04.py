# Conditional Execution

# hrs = input("Enter hours? ")
t = (hrs := float(input("Hrs "))) * (rph := float(input("Rph ")))
print(t if hrs <= 40 else t * 1.5)
