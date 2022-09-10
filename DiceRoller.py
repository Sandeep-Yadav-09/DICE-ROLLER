import random

# FUNCTIONS :
def one_dice() :

    D = random.randint(min_val, max_val)

    print("Dice is Rolling...")

    print("The value is :",D)

    if (D == 1) :
        print("Move", D, "Step Ahead ! ")
    else :
        print("Move",D, "Steps Ahead ! ")

    if D == 6 :
        print("Woohoo ! You got an Extra Turn .")

def two_dices() :

    print("Dice are Rolling...")

    print("The values are :")

    D1 = random.randint(min_val, max_val)
    D2 = random.randint(min_val, max_val)

    print("Dice 1 :",D1)

    print("Dice 2 :",D2)

    print("Move",(D1 + D2),"Steps Ahead ! ")

    if D1 == 6 and D2 == 6:
        print("Woohoo ! You got an Extra Turn.")

# MAIN CODE :

min_val = 1

max_val = 6

roll_again = "yes"

while roll_again.lower() == "yes" or roll_again.lower() == "y":

    print("\nHow many Dice you want to Roll ?")
    User = int(input())

    if (User == 1):
        one_dice()

    elif (User == 2):
        two_dices()

    else:
        print("Sorry ! This Option is not Available for Now.")

    roll_again = input("Roll the Dice Again ? (Yes/No) -> ")
    
    
