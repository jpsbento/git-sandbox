def total(pr, u):
    return pr * u

def mfunc():
    price=200
    units=5
    total_price = total(price, units)
    # A comment
    print("The total price is ", total_price, " pounds")

if __name__=='__main__':
    mfunc()
