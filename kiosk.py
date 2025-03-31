total = 0 

class kiosk:
    def __init__(self, item_price: float, item_name: str):
        self.item_price = item_price
        self.item_name = item_name

def main():
    global total  
    purchased_items = []
    while True:
        user_purchase = input('''Apple
Banana
Watermelon  
Milk
Ice Cream 
Chips 
What would you like to purchase?: ''').lower()

        if user_purchase == 'apple':
            apple = kiosk(4.99, 'Apple')
            total += apple.item_price 
            purchased_items.append((apple.item_name, apple.item_price))
        elif user_purchase == 'banana':
            banana = kiosk(3.89, 'Banana')
            total += banana.item_price
            purchased_items.append((banana.item_name, banana.item_price))
        elif user_purchase == 'watermelon':
            watermelon = kiosk(7.99, 'Watermelon')
            total += watermelon.item_price
            purchased_items.append((watermelon.item_name, watermelon.item_price))
        elif user_purchase == 'milk':
            milk = kiosk(6.79, 'Milk')
            total += milk.item_price
            purchased_items.append((milk.item_name, milk.item_price))
        elif user_purchase == 'ice cream':
            ice_cream = kiosk(9.79, 'Ice Cream')
            total += ice_cream.item_price
            purchased_items.append((ice_cream.item_name, ice_cream.item_price))
        elif user_purchase == 'chips':
            chips = kiosk(4.99, 'Chips')
            total += chips.item_price
            purchased_items.append((chips.item_name, chips.item_price))
        else:
            print("Invalid selection, please choose again.")
            continue

        print(f"Current total: {round((total),2)}")  

        user_continue = input('Would you like to continue shopping? (yes/no): ').lower()
        if user_continue == 'yes': 
            continue
        elif user_continue == 'no':
            user_payment = input('How would you like to pay? (card/cash): ').lower()
            if user_payment == 'card':
                card_number = input('Please provide a card number(**** **** **** ****): ')
                if len(card_number) > 18:
                    print('Invalid card number, purchase cancelled') 
                    break
                elif len(card_number) < 18:
                    print('Invalid card number, purchase cancelled') 
                    break
                else:
                    print("----- Inflation Market -----")
                    for item, price in purchased_items:
                        print(f"{item}: {price}")
                    print(f"Total: {total}")
                    print(f"Payment method: {user_payment.title()}")
                    print(f'Card number: {card_number}')
                    print("Change: 0.00")
                    print("-------------------")
                    print("Thank you for your purchase!")
                    break
            elif user_payment == 'cash':
                while True:
                    user_cash = int(input('How much cash do you have?: '))
                    cash = user_cash 
                    if cash < total:
                        print('Please provide more cash')
                        continue
                    elif cash >= total:
                        change = user_cash - total 
                        print("----- Inflation Market -----")
                        for item, price in purchased_items:
                            print(f"{item}: {price}")
                        print(f"Total: {total}")
                        print(f"Payment method: {user_payment}")
                        print(f"Change: {round((change),2)}")
                        print("-------------------")
                        print("Thank you for shopping with us")
                        break
        else:
            print('Invalid selection')
            continue
        break    
if __name__ == "__main__":
    main()