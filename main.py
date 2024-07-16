def total_price(price, units):
    return price * units

def main(price=100, units=3):
    print("The total price is %s" % total_price(price, units))

if __name__ == "__main__":
    main()

#comment