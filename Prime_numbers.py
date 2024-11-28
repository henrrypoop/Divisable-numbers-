#This is a script to determine prime numbers :D
'''
Built based on a logic that determines whether the input number is prime or not
Updates the variable to true if it is.
Then use another if condition to determine the prime number.
'''
from math import sqrt 

def divisable(numbers): #Define a print function for ease of access
    print(f"\n-Can {numbers} be divisable by 2 == 0:",numbers%2==0,f"\nor by 1:",numbers%1==0,f"\nor by itself:",numbers%numbers==0,"\n")

def prime():
    try:
        is_prime = True #assuming all input numbers are prime
        print("Determing prime numbers...")
        num = int(input("Enter a number here :"))

        if num > 2: # The input number has to be larger than 2
                for i in range(2,int(sqrt(num)+1)):
                    divisable(num) # calls the function  # a for loop that rune once to determine prime numbers               
                    if num % i == 0:                    
                        is_prime = False #Updates the variable
                    break #stops the loop once it has ran once
                    
                if is_prime: #if it's a prime number then:
                    print("--This is a prime number--\n")
                else: #if not then:
                    print("--This isn't a prime number--\n")

        else: #for the remaining cases where numbers are < 2.
            print(f"-- {num} is not a prime number.--\n")

    except ValueError as V: #returns an error if the input is not a number.
        print(f"You have not typed in a number\n, {V}")
prime()