#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D
#random module 
import random
user=0
#logic list used for making a matrix that can be accsessed by for getting Winning,Losing,Draw
logic=[["D","W","L"],["L","D","W"],["W","L","D"]]
user_score=0
user_life=3
comp_score=0
round=0
print("Welcome to Snake Water Gun Game 🐍🌊🔫!")
print("You have 3 lives. Win 10 rounds to win the game.")
#while loop to run the game for a certain limit
while True:
  #while loop will stop if user_life is 0 or user_score,comp_score is 10
  if(user_life==0):
    print("You have lost all your lives")
    break
  elif(user_score==10):
    print("You have won the game. Congratulations! 🏆")
    break
  elif(comp_score==10):
    print("Computer have won the game")
    break
  print("***********************************")
  round+=1
  print(f"Round {round}:")
  user_input=input("Enter your choice(Snake,Water,Gun):")
  print("-------------------------------------------")
  #this if else block is used to check user value and give it a number, later used a index
  if(user_input.capitalize()=="Snake" or user_input.upper()=="S"):
    print("You choose Snake")
    user=0
    
  elif(user_input.capitalize()=="Water" or user_input.upper()=="W"):
    print("You choose Water")
    user=1
  
  elif(user_input.capitalize()=="Gun" or user_input.upper()=="G"):
    print("You choose Gun")
    user=2
  #random value is used here to give comp a value
  comp=random.randint(0,2)
  if(comp==0):
    print("Computer chose Snake")
  elif(comp==1):
    print("Computer chose Water")
  elif(comp==2):
    print("Computer chose Gun")
  print("--------------------")
  #this 2D list is used to get the Value of the logic list
  ans=logic[user][comp]
  #here value stored on ans got checked and if it is D then it is a draw and if it is W then user wins and if it is L then
  if(ans=="W"):
    print("You have win this round")
    #if user win that round he will get 1 point
    user_score+=1
    #your score will be printed when you win that round
    print(f"Your score: {user_score}")
    
  
  elif(ans=="L"):
    print("You Lost this round")
    #if user lose that round he will lose 1 life
    user_life-=1
    #your life will be printed when you lose that round
    print("You have",user_life,"lives left")
    comp_score+=1
  
  elif(ans=="D"):
    print("It's Draw")
  print("***********************************")

