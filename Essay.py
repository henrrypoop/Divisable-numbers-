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
print("The original matrix is: \n",A,"\n")
print("A + A.T + CB + B.TxC.T is: \n",A + A.T + C@B + (B.T)@(C.T),"\n")

#b)
#Calculating A/10 + (A/11)^2 + (A/12)^3 + ... + (A/17)^8 + (A/18)^9 + (A/19)^10, and printing it to the screen

print("b)\n")
result = 0 
for i in range(10,20):
    power = i - 9 # Power starts at 1 for i = 10 and goes up to 10 for i = 19
    term = (A/i)**power 
    result += term
print("The original matrix is: \n",A,"\n")
print(f"\nCalculating A/10 + (A/11)^2 + (A/12)^3 + ... + (A/17)^8 + (A/18)^9 + (A/19)^10 is\n:{result}")

# saving odd integer numbers in the matrix A into a new vector, and printing the resultant vector to the screen.
print("c)\n")
c = []
c = A[A % 2 != 0] #Boolean indexing returns a flattened 1D array (vector)   
print("The original matrix is: \n",A,"\n")
print(c)

# saving prime numbers in the matrix A into a new vector, and printing the resultant vector to the screen.
print("d)\n")
d = []
def is_prime(number): # A function used to determine prime numbers
    if number < 2: # Prime numbers are numbers that is larger than 1 and only divisable by 1 and themselves.
        return False
    for i in range(2,int(np.sqrt(number))+1): #A for loop to check divisors up to sqrt(num)
        if number % i == 0:
            return False # returns False if there are divisors, then it's not prime
    return True #If no divisors are found, it's prime
    
#Iterating through the matrix to find a prime number:                        
for row in A: #Nested loop for iterating rows/nums inside the matrix
    for num in row:
        if is_prime(num): #check if the number(num) in each rows is prime
            d.append(num)
# Due to it being a list,the output will be: np.int32(...),np.int32(...),...
# Therefor we need to convert it into an array(vector):

vector_prime_d = np.array(d) # converting it into a vector
#print(A,"\n")            
#print(prime_A) outputs np.int32(...),np.int32(...),...
print("The original matrix is: \n",A,"\n")
print(vector_prime_d)
#Regarding the matrix A, find the rows which have maximum count of prime numbers, and print the rows to the screen.
print("e)\n")

prime_A_count = []
for row in A: #Nested loop for iterating rows/nums inside the matrix
    count = 0 # creates a counter for each row
    for num in row: # a loop for counting prime numbers
        if is_prime(num): #Counts primes in the rows
            count += 1 #increment of 1
    prime_A_count.append(count) #adds a counter to each rows

max_prime_count = max(prime_A_count) #the maximum number of prime numbers in any rows

'''#Enumerate is used when you want both value of the index and the row in a list or an array
for index,row in enumerate(prime_A_count): #Going through each indexes in each rows to compare max prime count
    if prime_A_count[index] == max_prime_count:
        print(f"row {i}: {row} with {max_prime_count} primes")
        '''
row_number = 0
print("The original matrix is: \n",A,"\n") 
#print(prime_A_count[1])
for row in A: 
    if prime_A_count[row_number] == max_prime_count: # checks if the current row has the maximum number of primes
        print(f"Row {row_number}: {row} with {max_prime_count} primes")
    row_number += 1 

#Regarding the matrix A, find the rows which have the longest contiguous odd numbers sequence, and print the rows to the screen.
print("f)\n")

def is_odd():
    for row in A:
        for num in row:
            num % 2 != 0 

def longest_odd_A_sequence(row):
    max_length = 0 # Stores the maximum length of consecutive odd numbers
    current_length = 0 #Tracks the current streak of odd numbers
    for num in row: # a loop for counting odds numbers
        if num % 2 != 0: #Counts odds in each rows
            current_length += 1 #increment of 1
            max_length = max(max_length,current_length) #Update maximum length
        else:
            current_length = 0 # Resets the streak if the number is even
    return max_length

#find rows with the longest contiguous odd sequence
longest_odd_rows = [] #Stores rows with the maximum contiguous odd sequence
max_odd_length = 0 #maximum length of contiguous odd sequence

for row in A:
    length = longest_odd_A_sequence(row) #Get the longest odd sequence in a row
    if length > max_odd_length:
        max_odd_length = length #Update the maximum length
        longest_odd_rows = [row] #Reset to only this row
    elif length == max_odd_length:
        longest_odd_rows.append(row) #Add this row to the list

print("The original matrix is: \n",A,"\n")
print(f"Rows with the longest contiguous odd numbers sequence (length {max_odd_length}):")
for row in longest_odd_rows:
    print(row)

###########PROBLEM: MATRICES THAT HAS NO PRIME OR ODDS NUMBERS AREN'T SOLVED YET###############
   