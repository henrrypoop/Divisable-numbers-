import numpy as np
A = [10,5,7,8,5]
int_A = [] #Initializing an empty list to store the indices value
'''
for i in range(len(A)): #Iterating through each elements in the input list A using a for loop.
    if A[i] == 5: #If the current element matches the target value,append it's index to the int_A
        print(i)
        int_A.append(i)
print(int_A)
'''
for num in A:
    if num % 2 != 0:
        int_A.append(num)
print(int_A)