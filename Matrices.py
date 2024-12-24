import numpy as np
from sympy import *
from scipy.linalg import svd
# sources: https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html#eigenvalues-eigenvectors-and-diagonalization
# https://www.geeksforgeeks.org/singular-value-decomposition-svd/
# HIGHLY UNDER DEVELOPMENT
# a rank 2 ,2x3 matrix
A = Matrix([[1,1,0],[0,1,1]])
A1 = np.array([[1,1,0],[0,1,1]])

# a rank 1 ,2x3 matrix
B = Matrix([[1,2,3],[2,4,6]])
B1 = np.array([[1,2,3],[2,4,6]])

names = ["A","B"]


def stuffs(anime,fart):
  print(f"Matrix {fart} is \n{np.array(anime)}\n")
  print(f"Reduced echelon form of matrix {fart}\n{np.array(anime)} is :\n",np.array(anime.echelon_form()),"\n")
  print(f"The rank of matrix {fart}\n{np.array(anime)} is :",anime.rank(),"\n")
  #AxA.T Part
  print(f"{fart} x {fart}.T is:\n",np.array(anime * anime.T),"\n")
  print(f"{fart}.T x {fart} is:\n",np.array(anime.T * anime),"\n")
  print("---------------------------------------------------------------------")

stuffs(A,names[0])
stuffs(B,names[1])

def calc(Mname,matrix,name):
  print(f"matrix {Mname}\n")
  print(f"{name} is:\n",np.array(matrix))
  print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&") 
  #print("The det of the given matrix:",matrix.det())
  print(f"The eigenvalues and eigenvectors of {name} is:\n{matrix.eigenvects()}\n")
  #Perform diagolization
  #P are eigenvectors, D are eigenvalues
  P, D = matrix.diagonalize()
  
  if name == "A*A.T" or name == "B*B.T":
    u1 = P[:,0]
    u2 = P[:,1]
    print("Let u1 be the eigenvector 1:\n",np.array(u1))
    print("Let u2 be the eigenvector 2:\n",np.array(u2),"\n")
  else:
    u1 = P[:,0]
    u2 = P[:,1]
    u3 = P[:,2]
    print("Let u1 be the eigenvector 1:\n",np.array(u1))
    print("Let u2 be the eigenvector 2:\n",np.array(u2))
    print("Let u3 be the eigenvector 3:\n",np.array(u3),"\n")

  #Checking for orthogonality
 
  if name == "A*A.T" or name == "B*B.T":
    if u1.dot(u2) == 0:
      print("orthogonality between u1 and u2 is TRUE\n")
    else:
      print("orthogonality between u1 and u2 is FALSE\n")
  else:
    if u1.dot(u2) == 0 and u1.dot(u3) == 0 and u2.dot(u3) == 0:
          print("orthogonality between u1 and u2 and u3 is TRUE\n")
    else:
          print("orthogonality between u1 and u2 and u3 is FALSE\n")

  #Normalizing the eigenvectors to form w1,|w2/ to form an orthogonal matrix that diagonalizes A.AT
  w1 = u1 / u1.norm()
  w2 = u2 / u2.norm()
  #Constructing Matrix U that will orthogonally diagonalizes A.AT
  U_ = Matrix.hstack(w1,w2)
  U , S, V = svd(A1)
  print("The matrix that orthogonally diagnoalizes A.AT is U=\n",np.array(U_),"\n")
  print("Left singular value of the matrix is:\n",U,"\n")
  print("Singular value of the matrix is:\n",S,"\n")
  print("Right singular value of the matrix is:\n",V,"\n")
  print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&") 

"""steve = A*A.T 
alex = B*B.T 
reverse_steve = A.T*A
reverse_alex = B.T*B

def results():
  print("\n")
  print(f"matrix {names[0]} is :                    \n{A1}")
  calc(steve,str(steve))
  print(f"inverse of matrix  {names[0]} is :                    \n{A1}")
  calc(reverse_steve,str(reverse_steve))

print("\n")
print(f"matrix {names[1]} is :                    \n{B1}")
calc(alex,str(alex))
calc(reverse_alex,str(reverse_alex))"""

calc("A",A*A.T,"A*A.T")
calc("A",A.T*A,"A.T*A")
calc("B",B*B.T,"B*B.T")
calc("B",B.T*B,"B.T*B")

