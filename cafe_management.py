# Define the manu of your cafe or shop
menu={
    'pizz' :   1000,
    "pasta" :   500,
    "Burger" :   400,
    "Mango Shake" :   200,
    "Cofee" :   100,
    "Shuwarma" :   350,
    "Zinger Burger" :   600,
    "Chicken Wrap" :   360,
    "Cold Drink" :   180,
    "Bana Shake" :   250,
}
# Greetings to userand user interface
print("Welcome to Talha's Resturent:  ")
for name, items in menu.items():
            print(f"{name}: {items}")

# print("Pizza: Rs 1000\nPasta: Rs 500\nBurger: Rs 400\nMango Shake: Rs 200\nCofee: 100\nShuwarma: Rs 350\nZinger Burger: Rs 600\nChicken Wrap: Rs 360\nCold Drink: Rs 180\nBanana Shake: Rs 250")


order_total=0

item_1=input("Enter the name of Item You Want to order: ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order.")

else:
    print(f"Ordered item {item_1} is not available Yet.")

another_item=input("Do you want to place another order Yes/No: ")
if another_item == "yes" :
    item_2=input("Enter the name of Second Item You Want to order: ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Your item {item_2} has been added to your order.")

    else:
        print(f"Ordered item {item_2} is not available Yet.")
else:
    print("Bye!")

print(f"The Total amount of items to pay is {order_total} ")

# finished


