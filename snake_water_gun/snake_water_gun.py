# Project 1 : Snake,water,Gun Game

# we all have played snake,water,gungame in our childhood.if you have't,google the rules of this game and write a python program capable of playing this game with the user

'''
1 for snake 
-1 for water 
0 for gun
'''

import random
computer = random.choice((-1,1,0))
youstr=input("Enter your choice(s/w/g):")
youDict = {"s":1,"w":-1,"g":0}
reverseDict={-1:"Water",1:"Snake",0:"Gun"}

if youstr not in youDict:
    print("Invalid choice!")
else:
    you = youDict[youstr]
    # print("Your choice value:", you)
    print(f"YOU CHOICES: {reverseDict[you]} \nCOMPUTER CHOICES: {reverseDict[computer]}") 


# you = youDict[youstr]
    if(computer == -1 and you == 1):
       print("YOU WIN!")

    elif(computer == -1 and you == 0):
      print("COMPUTER WIN!")    

    elif(computer == -1 and you == -1):
     print("TIE")

    elif(computer == 1 and you == 0):
     print("YOU WIN!")      

    elif(computer == 1 and you == -1):
     print("COMPUTER WIN!")   

    elif(computer == 1 and you == 1):
     print("TIE") 

    elif(computer == 0 and you == -1):
     print("YOU WIN!")     

    elif(computer == 0 and you == 1):
     print("COMPUTER WIN!")  

    elif(computer == 0 and you == 0):
     print("TIE") 
 
# elif((computer == 1 and you == 1) or (computer == -1 and you == -1) or (computer == 0 and you == 0) ):
#     print("TIE") 

    else:
     print("------SOMETHING WENT WRONG------")




