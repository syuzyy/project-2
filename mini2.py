import random

def roll_dice():
    return random.randint(1, 6)

#In the context of the game, the roll_dice() function is called twice for each roll to simulate the two dice being rolled,
#and the results are added together to get the total sum of the dice rolls.

def main():
    while True:
        input("Press Enter to roll the dice...")
        dice1 = roll_dice()     # Roll the first die
        dice2 = roll_dice()     # Roll the second die
        total = dice1 + dice2   #the sum of the dice rolls
        print(f"You rolled: {dice1} + {dice2} = {total}")
        
        if total in (7, 11):
            print("Congratulations! You win!")
            break
        elif total in (2, 3, 12):
            print("Sorry, the casino wins.")
            break
        else:
            goal = total
            print(f"Your goal is now {goal}. Keep rolling...")   
# the f before the string indicates that the curly braces {} should be replaced
# with the value of the goal variable. 
            while True:
                input("Press Enter to roll the dice...")
                dice1 = roll_dice()
                dice2 = roll_dice()
                total = dice1 + dice2
                print(f"You rolled: {dice1} + {dice2} = {total}")
                
                if total == 7:
                    print("Sorry, you lose.")
                    break
                elif total == goal:
                    print("Congratulations! You win!")
                    break

if __name__ == "__main__":
    print("Welcome to the Dice Rolling Game!")
    print("Roll two dice and follow the rules to win or lose.")
    main()
    input("Press Enter to exit...")