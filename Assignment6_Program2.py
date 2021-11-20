"""ASS6 PROG2
Program 2: Addition Trainer
Create a program that automatically generate two random numbers to add (0 to 99)
Let the user answer and evaluate if the user has the correct answer
The program will ask the user 10 addition operation
Display the result summary of the 10 operations (ex 9/10)"""

#Ass6 Prog2, 1st try,   

import random

#0 starters
QuestionNum = 0
CurrentScore = 0
print("\nSolve for the following y. Goodluck!\n")

#1 ask question 10 times with user input, score tally, and question number tally
while QuestionNum != 10:                        #loop until 10 questions
    QuestionNum = QuestionNum + 1               #question number counter
    Addend1 = random.randint(0,99) 
    Addend2 = random.randint(0,99) 
    print(f"Question #{QuestionNum}\n{Addend1} + {Addend2} = y")      
    CorrectAnswer = Addend1 + Addend2 
    UserAnswer = int(input("y  =  "))                                 
    if CorrectAnswer == UserAnswer:                                    
        print("✓ Correct! ✓\n")
        CurrentScore = CurrentScore + 1          #score tally
    else: 
        print(f"✘ Wrong! ✘ \nThe correct value for y is {CorrectAnswer}.\n")

#2 display final score n description
print(f"You got {CurrentScore} correct answer(s) and {10 - CurrentScore} wrong answer(s).\nYou scored {CurrentScore}/10.\n")