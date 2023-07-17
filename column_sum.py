R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")
for i in range(R):
    a =[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
n = len(matrix)
m=len(matrix[0])
lst=[]
for  k in range(m):
    sum_=0
    for l in range(n):
        sum_+=matrix[l][k]
    lst.append(sum_)
print(lst)