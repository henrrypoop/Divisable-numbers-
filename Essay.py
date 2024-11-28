#Essay :D
import math, numpy as np , sympy as sy, matplotlib
#Task 1
print("Task 1:")
#Creating a random 10 x 10 matrix A with random integers in [1,100], a 2 x 10 matrix B with random integers in [1,20], and a 10 x 2 matrix C random integers in [1,20]
A = np.random.randint(1,101, size =(10,10))
B = np.random.randint(1,21, size =(2,10))
C = np.random.randint(1,21, size =(10,2))
#a)
#Calculating A + A.T + CB + B.TxC.T, and printing the result to the screen
# @ is similar to np.dot

print("a)\n")
##print("A + A.T + CB + B.TxC.T is: \n",A + A.T + C@B + (B.T)@(C.T),"\n")
#b)
#Calculating A/10 + (A/11)^2 + (A/12)^3 + ... + (A/17)^8 + (A/18)^9 + (A/19)^10, and printing it to the screen

print("b)\n")
result = 0 
for i in range(10,20):
    power = i - 9 # Power starts at 1 for i = 10 and goes up to 10 for i = 19
    term = (A/i)**power #previously tried using result += ... >> Wrong calculations due to python rounding up numbers
    #So putting it into another variable and then adding up that variable in the result works instead
    #print(f"i is: {i} so:\n {term}") For debugging in each loops
    result += term
##print(f"\nCalculating A/10 + (A/11)^2 + (A/12)^3 + ... + (A/17)^8 + (A/18)^9 + (A/19)^10 is\n:{result}")

# saving odd integer numbers in the matrix A into a new vector, and printing the resultant vector to the screen.
print("c)\n")
'''int_A = []
for row in A: # iterating through each rows of the matrx
    for num in row: # looping through each numbers in the row
        if num % 2 != 0: # checks if the number is odd
            int_A.append(num)
print(int_A)'''
int_A = A[A % 2 != 0] 
x = np.array(int_A) #turning the list into a vector    
print(x)
