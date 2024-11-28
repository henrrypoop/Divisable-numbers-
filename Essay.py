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
#print("A + A.T + CB + B.TxC.T is: \n",A + A.T + C@B + (B.T)@(C.T),"\n")
#b)
#Calculating A/10 + (A/11)^2 + (A/12)^3 + ... + (A/17)^8 + (A/18)^9 + (A/19)^10, and printing it to the screen
print("b)\n")
n = 10
x = 1
z = ((5/(n+1))**(x+1))
for i in range(n,20):
    print(z)