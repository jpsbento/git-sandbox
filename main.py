from utils import *

def mfunc(price=200,units=5):
    tot = tot(price, units)
    tot_eur = tot(price*1.2,units)
    print("The total price is ", tot, " pounds")
    print("And that is equivalent to ", tot_eur, " euros")

mfunc()
