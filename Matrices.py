import numpy as np
from sympy import *
from scipy.linalg import svd
#Rank 0
# sources: https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html#eigenvalues-eigenvectors-and-diagonalization
# https://www.geeksforgeeks.org/singular-value-decomposition-svd/
A = Matrix([[3,2,2],[2,3,-2]])
A1 = np.array([[3,2,2],[2,3,-2]])

print("The maxtrix given:\n",np.array(A))
print("Reduced echelon form of the given matrix:\n",A.echelon_form(),"\n")
print("The rank of the matrix:",A.rank(),"\n")

#AxA.T Part
print("AxA.T is:\n",np.array(A * A.T),"\n")
print("                          AxA.T is:")
def calc(matrix,name):
  print("---------------------------------------------------------------------")
  #print("The det of the given matrix:",matrix.det())
  print(f"The eigenvalues and eigenvectors of {name} is:\n{matrix.eigenvects()}\n")
  #Perform diagolization
  #P are eigenvectors, D are eigenvalues
  P, D = matrix.diagonalize()
  #Let u1,u2 be:
  u1 = P[:,0]
  u2 = P[:,1]

  print("Let u1 be the eigenvector 1:\n",np.array(u1))
  print("Let u2 be the eigenvector 2:\n",np.array(u2),"\n")

  #Checking for orthogonality
  def orthogonality_check(a,b):
    if a.dot(b) == 0:
      return True
    else:
      return False

  print("orthogonality between u1 and u2 is:",orthogonality_check(u1,u2),"\n")

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
  print("---------------------------------------------------------------------")
calc(A*A.T,"A*A.T")
print("                          A.TxA is:")
calc(A.T*A,"A.T*A")
