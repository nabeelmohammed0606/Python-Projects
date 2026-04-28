#cash register simple

item_price = float(input("Enter the price of the item: "))
item_quantity = int(input("Enter the quantity of the item: "))

total = item_price * item_quantity 

print(f"Total: ${total}")