import sys
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question (press enter to exit)")
   
    answer = random.randint(1,8)
   
    if question =="":
        sys.exit()
    
    elif answer == 1:
      print("probably")
    
    elif answer == 2:
      print("it's looking real good for you")

    elif answer == 3:
      print("I'd say so")
    
    elif answer == 4:
      print("Ask again later")
    
    elif answer == 5:
      print("Concentrate and ask again")
    
    elif answer == 6:
      print("Stupid question, try again")
  
    elif answer == 7:
      print("no")
   
    elif answer == 8:
      print("Probably maybe possibly no")
  