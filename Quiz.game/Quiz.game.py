# a = 33
# b = 200
# def new_func():
#     print("b is greater than a")
#     print(f"b is {200} and a is {23}")

# if b > a:
#   new_func()

print("Welcome to the Quiz game.")

print("Would you like to play the game?")

playgame= input("Type Yes to continue and No to quit: ")

if playgame.lower()!="Yes": #Boolean checker 
    quit()
    

print("Okay! Let's play :)")

answer= input("What does CPU stand for? ") #Question 1
if answer.lower == "central processing unit":
    print("Correct!")  
else:
    print("Incorrect :(")
    
answer= input("What does PSU stand for? ") #Question 2
if answer == "PSU":
    print("Correct!")
else:
    print("Incorrect :(")
    
answer= input("What does RAM stand for? ") #Question 3
if answer == "random access memory":
    print("Correct!")   
else:
    print("Incorrect :(")
    

answer= input("What does GPU stand for? ") #Question 4
if answer == "graphics processing unit":
    print("Correct!")    
else:
    print("Incorrect :(")
    


    
    
    
