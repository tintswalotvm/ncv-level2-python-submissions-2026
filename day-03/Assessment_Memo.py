#Level two Python assessment
#student number
vat = 0.15
first_name = input("Enter name and surname: ")
itemPrice1 = float(input("Enter price of first item "))
itemPrice2 = float(input("Enter price of second item "))
first_name = first_name.upper()

total = itemPrice1 + itemPrice2
amountDue = total + (total*vat)

print("The total is: ",f"{total:.2f}")
print("The amount due is: ",f"{amountDue:.2f}")

print("Thank you, call again: " + first_name)