def place_order(item):
    print(f'Order placed: your order is {item}')
    
    #eggs => 4
    #tot = (base_price  + 5) * 1.15
    def calculate_total(item):
        prce = 25.5
        Vat = 0.15
        totalPrice = (base_price + len(item)) * 1.15
        return totalPrice
  
def get_order():
    print('preparing order...')
    return'collect your order'
   
myFood = input('what would you like?')
place_order(myFood)

print(get_order())

order_total = calculate_total(myFood)
print(f'your order costs: R{round(order_total,2)}')



    

    