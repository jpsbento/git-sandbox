def total_price(price, units):
    if units < 1.:
        print("Not a valid unit value!")
    else:
        return price * units

def main(price=100, units=3):
    print("The total price is %s" % total_price(price, units))

if __name__ == "__main__":
    main()
    
# This is a comment that is common to Marina and Joao