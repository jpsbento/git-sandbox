def tot(pr, u):
    return pr * u

def mfunc():
    price=200
    units=5
    tot = tot(price, units)
    tot_eur = tot(price*1.2,units)
    print("The total price is ", tot, " pounds")
    print("And that is equivalent to ", tot_eur, " euros")

if __name__=='__main__':
    mfunc()

#now will define a second function calling the same tot function to define a new total price in dollars 
def mfunc2():
    price=300
    units=6
    tot = tot(price, units)
    print("The total price is ", tot, "dollars")

mfunc2()