import numpy as np
rows=int(input("Enter the no of rows:"))
cols=int(input("Enter the no of columns:"))
print("\nEnter the elaments of matrix A : ")
A=[list(map(int,input().split()))for i in range(rows)]
A=np.array(A)
print("\nEnter the elaments of matrix B : ")
B=[list(map(int,input().split()))for i in range(cols)]
B=np.array(B)
print("\n Matrix A:\n",A)
print("\n Matrix B:\n",B)
print("\n Addition:\n",A+B)
print("\nSubtraction:\n",A-B)
print("\n Element Wise multiplication:\n",A*B)
print("\nMatrix Multiplication:\n",np.dot(A,B))
print("\nTranspose of Matrix A:\n",A.T)
print("sum of Matrix B:\n",np.sum(B))
print("\nMean of matrix B:\n",np.mean(B))