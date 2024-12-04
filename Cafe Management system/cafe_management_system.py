menu={
    "pizza":40,
    "pasta":50,
    "Burger":50,
    "salad":90,
    "coffee":30,
}
print("Welcome to SanelyInsane cafe")
print("pizza: Rs40,\n pasta:Rs50,\n Burger:50,\nsalad:90,\n coffee:30")
order_total=0
item_1=input(("Enter the name of item you want to order="))
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your {item_1} has been added to the order")
else:
    print("Ordered item is not available")
another_order=input("Do You want to order anything else:yes/No")
if another_order=="yes":
    item_2=input("Enter your second order=")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print("ordered item is not available!")
print("Total amount of order to pay  is",order_total)