#Start
shopping_cart = []
price_list = []
print()
print("You have a standard shopping cart with zero items.")
print("Your shopping list is Rat Poison, Mouse Poison and Cheese (For the mouse trap)")
print("Current Prices: Apples:$1, Rat Poison:$67, Oranges:$1, Mouse Poison:$69, Bananas:$1, Cheese:$420")
print()
print ("Choose an option:\n1.Add item to cart\n2.Remove item from cart\n3.Clear cart and restart\n4.View total and checkout")
choice = input().lower().strip()
    # ---------------------------------------
while True:
        
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
        if choice in ('1' or '1.' or 'option 1' or 'one'):
            item = input("What item would you like to add?\n")
            shopping_cart.append(item)
            price = input ("How much is that?\n")
            price_list.append(float(price))
                


    # -----------------------------------------------------------------
    # OPTION 2: REMOVE ITEM 
    # -----------------------------------------------------------------
        elif choice in ('2' or '2.' or 'option 2' or 'two'):
            remove_item = input("What item do you want to remove?")
            Removed_item = shopping_cart.index(remove_item)
            shopping_cart.remove(remove_item)
            price_list.pop(Removed_item)
                
    # ----------------------------------------------------------------
    # OPTION 3: CLEAR CART (Practice clearing a list)
    # -----------------------------------------------------------------
        elif choice in ('3' or '3.' or 'option 3' or 'three'):
            shopping_cart.clear()
            price_list.clear()
            print ("Your cart is empty")
              
    # -----------------------------------------------------------------
    # OPTION 4: CHECKOUT
    # -----------------------------------------------------------------
        elif choice in ('4' or '4.' or 'option 4' or 'four'):
            total_cost = sum(price_list)
            print(f"Your total cost is ${total_cost}\nNow is that cash or card?")
            break
       

    # -----------------------------------------------------------------
    # NO OPTION
    # -----------------------------------------------------------------
        else:
            print("Your option is not valid")
            
