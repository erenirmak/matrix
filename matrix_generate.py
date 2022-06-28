temp = []
matrix = []
for i in range(4):
    x = int(input())
    temp.append(x)
    if len(temp) == 2:
        matrix.append(temp) #without adding .copy() to the temp, matrix also cleared
        temp.clear()

print(matrix)
