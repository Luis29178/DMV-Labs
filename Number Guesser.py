import random

win = False

name = input("Enter your name: ")

mynum = random.randint(1,20)

print("Hello "+name+" guess a number beywene 1 and 20")

num = input("Answer: ")

while not win:
    if int(num) > mynum:
        num = input("Too large try again: ")
    elif int(num) < mynum:
        num = input("Too small try again: ")
    elif int(num) == mynum:
        print("Congrats you got it!!!!")
        win = True
 
 
 
