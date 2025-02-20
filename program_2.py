# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#Tanner Rosenthal
#2/20/2025

import random

def quiz():
    random1 = random.randint(100, 999)
    random2 = random.randint(100, 999)
    print("     ", random1)
    print("+    ", random2)
    print("---------")

    user_answer = int(input("what is the answer?"))
    correct_answer = random1 + random2

    if user_answer == correct_answer:
        print("That is correct!")

    else:
        print("That is incorrect. The correct answer is", correct_answer)

quiz()
