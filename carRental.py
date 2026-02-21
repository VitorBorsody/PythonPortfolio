kilometersDriven = float(input('Enter the kilometers driven:'))
rentalDays = int(input('Enter the rental days: '))
totalCost = rentalDays*60 + kilometersDriven*0.15
print(f"Total cost is ${totalCost:.2f}")