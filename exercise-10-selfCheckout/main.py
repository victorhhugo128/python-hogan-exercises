price = ['0']
quantity = ['0']
i = 0

price[i] = input("Enter the price of the product {}: ".format(i + 1))
quantity[i] = input("Enter the quantity of product {}: ".format(i + 1))

while True:
  option = input("Would you like to add another product? ")
  if option.lower() == "yes":
    i += 1
    price.append(input("Enter the price of the product {}: ".format(i + 1)))
    quantity.append(input("Enter the quantity of product {}: ".format(i + 1)))
  elif option.lower() == "no":
    break
  else:
    print("Please enter a valid asnwer(yes or no).")

tax = 0.055
subtotal = 0
for i in range(0, len(price)):
  subtotal += float(price[i]) * float(quantity[i])

print(f"""Subtotal: {subtotal:.2f}
Tax: {tax*subtotal:.2f}
Total: {(subtotal + subtotal*tax):.2f}""")