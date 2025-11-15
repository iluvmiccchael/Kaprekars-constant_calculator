#-------------------------------------------------------
# KAPREKAR'S CONTANT CALCULATOR 
# ------------------------------------------------------
import random

def kaprekar_step(n):
    digits = f"{n:04d}"
    desc = int("".join(sorted(digits, reverse = True)))
    asc = int ("".join(sorted(digits)))

    return desc - asc 

def kaprekar_process(n):
    print(f"starting number: {n}")

    if len(set(str(n))) == 1:
        print("all digits are equal and will there always produce zero")
        return
    steps = 0

    while n != 6174:
        n = kaprekar_step(n)
        steps += 1
        print (f"step {steps}: {n}")

    print(f"n\ you have reached kaprekar's constant: 6174")


#user input
print("-------------------------------------------------------")
print("KAPREKAR'S CONTANT CALCULATOR ")
print("-------------------------------------------------------")
 
number = random.randint(1000,9999)
print (f'the random number is {number}')


kaprekar_process (number)