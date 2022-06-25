'''This File calculates the tax and shipping costs of a product'''

def calc_tax(product):
    tax = product * .07
    return float(tax), float(product)


productcost = calc_tax(float(input("what is the cost of the product:")))
tax = productcost[0]


def calc_shipping(product_weight):
    if product_weight <= 20:
        shipping =   10
    else:
        shipping =  20
    return shipping

shippingcost = calc_shipping(int(input("what is the wieght:"))) 

total = productcost[0] + shippingcost +productcost[1]
print()
print(f"your product cost ${productcost[1]}\n")
print(f"your tax of 7 pecent added ${tax:.4f} to your cost\n")
print(f"and your shipping was ${shippingcost} so your total is \n")
print(f"total cost is ${total:.2f}")
