#define a function that takes two arguments, price and units
#the function should return the total price
def tot(pr, u):
    return pr * u

# define a function that calls the tot function
# the function should print the total price
def mfunc():
    price=200
    units=5
    tot = tot(price, units)
    print("The total price is ", tot, " pounds")

mfunc()

#now will define a second function calling the same tot function to define a new total price in dollars 
def mfunc2():
    price=300
    units=6
    tot = tot(price, units)
    print("The total price is ", tot, "dollars")

mfunc2()