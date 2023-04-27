import sys
import random
from time import sleep

print("ROCK!\tPAPER!\tSCISSORS")
def jokenpo(user_choice):
    sleep(0.1)
    print(f'\n==================================================\n')
    sleep(0.5)
    print('ROCK!')
    sleep(0.5)
    print('PAPER!')
    sleep(0.5)
    print('SCISSORS!')
    sleep(0.5)
    print(f'==================================================\n\n')
    sleep(0.1)

    cpu_choice = random.randint(0,2)

    if user_choice == 0:
        print(f'You chose ROCK')
    elif user_choice == 1:
        print(f'You chose PAPER')
    else:
        print(f'You chose SCISSORS')

    if cpu_choice == 0:
        print(f'\n\n\nComputer chose ROCK')
    elif cpu_choice == 1:
        print(f'\n\n\nComputer chose PAPER')
    else:
        print(f'\n\n\nComputer chose SCISSORS')

    compare(user_choice, cpu_choice)

def compare(user_choice, cpu_choice):
    if user_choice == cpu_choice:
        print(f'\n\nIT\'S A TIE!\n')
    elif user_choice == 0 and cpu_choice == 1:
        print(f'\n\n\nPaper covers rock.')
        print(f'\n\nYOU LOSE!\n')
    elif user_choice == 0 and cpu_choice == 2:
        print(f'\n\n\nRock smashes scissors.')
        print(f'\n\nYOU WIN!\n')
    elif user_choice == 1 and cpu_choice == 0:
        print(f'\n\n\nPaper covers rock.')
        print(f'\n\nYOU WIN!\n')
    elif user_choice == 1 and cpu_choice == 2:
        print(f'\n\nScissors cuts paper.')
        print(f'\n\nYOU LOSE!\n')
    elif user_choice == 2 and cpu_choice == 1:
        print(f'\n\nScissors cuts paper.')
        print(f'\n\nYOU WIN!\n')
    else:
        print(f'\n\nRock smashes scissors.')
        print(f'\n\nYOU LOSE!\n')
    print(f'\n==================================================\n')
    again=int(input("Wanna play again?\n1-yes\t2-no\n"))
    if again==1:
        main()
    elif again==2:
        sys.exit()
    
    
def main():
    user_choice = ''
    valid_choices = [0, 1, 2]
    while user_choice not in valid_choices:
        user_choice = int(input('What do you choose?\n\
            0 - Rock\n\
            1 - Paper\n\
            2 - Scissors\n'))
        if user_choice in valid_choices:
            jokenpo(user_choice)

main()

    
    
