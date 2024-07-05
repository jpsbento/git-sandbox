def tot(pr, u):
    return pr * u

def mfunc():
    price=200
    units=5
    total = tot(price, units)
    print("The total price is ", total, " pounds")

if __name__=='__main__':
    mfunc()
