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

if playgame.lower()!="yes": #Boolean checker 
    quit()
    

print("Okay! Let's play :)")

score=0
print(score)

answer= input("What does CPU stand for? ").lower() #Question 1
if answer == "central processing unit":
    print("Correct!")  
    score+=1
else:
    print("Incorrect :(")
    
answer= input("What does PSU stand for? ") #Question 2
if answer.lower() == "psu":
    print("Correct!")
    score+=1
else:
    print("Incorrect :(")
    
answer= input("What does RAM stand for? ") #Question 3
if answer.lower() == "random access memory":
    print("Correct!")
    score=score+1
else:
    print("Incorrect :(")
    

answer= input("What does GPU stand for? ") #Question 4
if answer.lower() == "graphics processing unit":
    print("Correct!")   
    score=score+1
else:
    print("Incorrect :(")
    
print(f"Your total score for the test is {score} and you got {score} questions correct")
print(f"you got {(score/4)*100}% of the questions correct")
print("Game over. Thank you taking the Quiz!!!")

