def total_price(price, units):
    return price * units

def main():
    price = 100
    units = 3
    print("The total price is %s" % total_price(price, units))

if __name__ == "__main__":
    main()


test=total_price(1,100)
print(test)

test2=total_price(2,100)
print(test)
#comment