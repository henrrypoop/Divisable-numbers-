import numpy as np
from sympy import *
from scipy.linalg import svd
# sources: https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html#eigenvalues-eigenvectors-and-diagonalization
# https://www.geeksforgeeks.org/singular-value-decomposition-svd/
# HIGHLY UNDER DEVELOPMENT
# a rank 2 ,2x3 matrix
A = Matrix([[4,1,2],[1,4,-2]])
A1 = np.array([[4,1,2],[1,4,-2]])

# a rank 1 ,2x3 matrix
B = Matrix([[3,3,3],[6,6,6]])
B1 = np.array([[3,3,3],[6,6,6]])

names = ["A","B"]
# Testing
#A = Matrix([[3,2,2],[2,3,-2]])
#A1 = np.array([[3,2,2],[2,3,-2]])

def stuffs(anime,fart):
  print(f"Matrix {fart} is \n{np.array(anime)}\n")
  print(f"Reduced echelon form of matrix {fart}\n{np.array(anime)} is :\n",np.array(anime.echelon_form()),"\n")
  print(f"The rank of matrix {fart}\n{np.array(anime)} is :",anime.rank(),"\n")
  #AxA.T Pa
  print(f"{fart} x {fart}.T is:\n",np.array(anime * anime.T),"\n")
  print(f"{fart}.T x {fart} is:\n",np.array(anime.T * anime),"\n")
  print("---------------------------------------------------------------------")

stuffs(A,names[0])
stuffs(B,names[1])

def calc(Mname,matrix,name):
  #Accessing the variable A using globals()
  A_matrix = globals()[Mname]
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
    v1 = (P[:, 0]).T
    v2 = (P[:, 1]).T
    v3 = (P[:, 2]).T
    V_1 = np.array(Matrix.vstack(v1,v2,v3))
    a1 = V_1[0,:]
    a2 = V_1[1,:]
    a3 = V_1[2,:]
    #print(a1,"\n",a2,"\n",a3,"\n")
    #print("Testing",V_1)
    print("v2 is:/n",(np.dot(a2,a1)/np.dot(a1,a1))*a1)
    print("v3 is:/n",(np.dot(a3,a2)/np.dot(a2,a2))*a2)
  #Checking for orthogonality

  if name == "A*A.T" or name == "B*B.T":
    if u1.dot(u2) == 0:
      print("orthogonality between u1 and u2 is TRUE\n")
    else:
      print("orthogonality between u1 and u2 is FALSE\n")

  #Normalizing the eigenvectors to form w1,|w2/ to form an orthogonal matrix that diagonalizes A.AT
  subname = {}
  if name == "A*A.T" or name == "B*B.T":
    w1 = u1 / u1.norm()
    w2 = u2 / u2.norm()
    U_ = Matrix.hstack(w1,w2)
    subname = "U"
    print(f"The matrix that orthogonally diagonalizes {name} is \nU=\n",np.array(U_),"\n")
    print(f"and the diagonal matrix is: {subname}^T({name}){subname} = D = \n",U_.T*matrix*U_)
  else: # For A.T x A or B.T x B
    v1 = v1.T / Matrix(v1).norm()
    v2 = v2.T / Matrix(v2).norm()
    v3 = v3.T / Matrix(v3).norm()
    V_ = Matrix.hstack(v1,v2,v3)
    subname = "V"
    print(f"The matrix that orthogonally diagonalizes {name} is \nV=\n",np.array(V_),"\n")
    print(f"and the diagonal matrix is: {subname}^T({name}){subname} = D = \n",V_.T*matrix*V_)

  #Constructing Matrix U that will orthogonally diagonalizes A.AT/AT.A
  U , S, V = svd(A_matrix)
  print(f"Left singular vectors of matrix {Mname} is:\nU=\n",U,"\n")
  print(f"Singular value of matrix {Mname} is:\nS=\n",S,"\n")
  print(f"Right singular vectors of matrix {Mname} is:\nV.T=\n",V,"\n")
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

calc("A1",A*A.T,"A*A.T")
calc("A1",A.T*A,"A.T*A")
calc("B1",B*B.T,"B*B.T")
calc("B1",B.T*B,"B.T*B")
