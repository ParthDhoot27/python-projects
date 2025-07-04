import random
while True:
    while True:
        #error handling and getting computer choice 
        try:
            computer_choice = int(random.randint(1, 100))
            break
        except:
            print("invalid input re-enter")
    chances_played = 0
    while True :
        # getting user choice 
        try:
            user_choice = int(input("please enter a number between 1 to 100 : "))
            chances_played += 1
        except:
            print("invalid input re-enter")
            continue
        # user choices cases
        if(user_choice>100 or user_choice<1):
            print("please enter a valid choice:")
        elif(user_choice == computer_choice):
            #winning case
            print("you win..")
            print(f"your rating is {(10/chances_played)} out of 10")
            print("you are not too lucky to get a rating of 2.5 i.e clear game in 4 guesses. Are You?")
            break
        elif(user_choice < computer_choice + 7 and user_choice > computer_choice):
            print("close but little higher!! you can guess it")
        elif(user_choice > computer_choice - 5 and user_choice < computer_choice):
            print("close but little lower!! you can guess it")
        elif(user_choice > computer_choice + 7 ):
            print("too High !")
        elif(user_choice < computer_choice - 5):
            print("too low !")
        
    # play again 
    replay = input("do you want to play again? (enter y to play , any other key to exit)").lower()
    if(replay == "y"):
        continue     
    else:
        print("thanks for playing")
        break
    
