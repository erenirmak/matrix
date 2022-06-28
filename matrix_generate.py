temp = []
matrix = []
n = int(input("matrix degree: "))
for i in range(n):
    x = int(input())
    temp.append(x)
    if len(temp) == n:
        matrix.append(temp) #without adding .copy() to the temp, matrix also cleared
        temp.clear()

print(matrix)
