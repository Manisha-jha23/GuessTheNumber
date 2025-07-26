import random

target=random.randint(1,100)
while True:
    userchoice=input("Guess the target number or Quit(Q): ")
    if(userchoice=="Q"):
        break
    userchoice=int(userchoice)

    if(userchoice==target):
        print("Success : Correct Guess!! ")
        break
        
    elif(userchoice<target):
        print("Your guessed number is too small ..Guess again ")
    else:
        print("Your guessed number is too big ..Guess again ")
print("___GAME OVER____")
    