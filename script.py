#Input variables
meal = input('How much was your meal, not including tax? ')
tax = input('How much was tax? ')
tip = input('How much would you like to tip? (%) ')

#Convert tip input to float
tip = float(tip)
tip = tip / 100

#Compute dollar value of tip and total
tip = tip * meal
meal = meal + tip
total = meal + tax

#Print outputs for user
print('Tip:', "%.2f" % tip)
print('Total:', "%.2f" % total)
