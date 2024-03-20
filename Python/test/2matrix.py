#转置矩阵
matrix_copy=[[row[i] for row in matrix] for i in range(len(matrix))]

#格式化输出矩阵
for m in range(len(matrix)):
    for n in range(len(matrix[0])):
        print(matrix[m][n],end=" ")
    print("\n")
