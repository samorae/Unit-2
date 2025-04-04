import random


def rand_tick():
    random_ticket = [1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E']
    my_ticket = random.sample(random_ticket, 4)
    print(*my_ticket)
    return my_ticket

def lottery_game(random_numbers):
    random_ticket = [1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E']
    account_balance = 1000000
    while True:
        lottery_machine = random.sample(random_ticket, 4)
        print("Rolling!")
        print(f'Your numbers were {random_numbers}, the Machines number was {lottery_machine}')
        account_balance = account_balance - 15
        print(f'Your money left is {account_balance}')
        if random_numbers == lottery_machine:
            print('______WINNER______')
            break 
        else:
            print('______LOSER______')
            user_choice = input('Do you wanna continue, yes or no?: ').strip().lower()  
            if user_choice == 'yes':
                continue
            elif user_choice == 'no':
                print('Goodbye')
                break
            else:
                print('Invalid input. Please enter yes or no.')
            break 

def main():
    random_numbers = rand_tick()
    lottery_game(random_numbers)

if __name__ == '__main__':
    main()

