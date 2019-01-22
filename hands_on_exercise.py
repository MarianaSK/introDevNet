"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi), pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print(i)
if i<50:
    print("i eh menor que 50")
elif i>50:
    print("i eh maior que 50")
else:
    print("i eh igual a 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print(picked_fruit)
if picked_fruit!='banana':
    print("nao eh banana")
else:
    print("eh banana")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multi (a, b):
    result=a*b
    print(a, " x ", b, " = ", result)
    return result


# TODO: Now call the function a few times to calculate the following answers
multi(12, 96)
multi(48, 17)
multi(196523, 87323)
#print("12 x 96 =",)

#print("48 x 17 =",)

#print("196523 x 87323 =",)