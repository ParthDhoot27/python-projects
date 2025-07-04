import random

#choose total no of dices you want to roll 
while True:
    #error handling
    try:
        no_dices = int(input("enter no of dices you want to roll? : "))
        break
    except:
        print("invalid input re-enter")
# chances played initally 0 
chances_played = 0

#infinite while loop
while True :
    #list to carry rolled dice no 
    dice_no = []
    # user input to start
    to_play = input("do you want to roll the dice? (y/n) : ").lower()

    if(to_play == "y"):
        #append no of random choices in list
        for i in range(no_dices):
            dice_no.append(random.randint(1, 6))
        print(dice_no)
        #increament in chancwes played
        chances_played += 1
        print(f"{chances_played} chances are played")
    elif(to_play == "n"):
        print("program closed...")
        print(f" total {chances_played} chances were played")
        break
    else:
        print("invalid input Re-Enter ")

