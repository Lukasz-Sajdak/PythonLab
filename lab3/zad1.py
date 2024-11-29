def matrix_multiplying(matrix1, matrix2):
    counter = 0
    if len(matrix1) != len(matrix2[0]):
        print("ERROR")
    else:
        for i in range (len(matrix1)): # 2
            for j in range(len(matrix2[0])): # 2
                for k in range(len(matrix2)): # 3
                    out[i][k] += (matrix1[i][k]*matrix2[k][j])

    return out

matrix1 = [[1,2,3], [1,4,5]]
matrix2 = [[2,3], [5,3], [1,5]]

out= [[0,0,0], [0,0,0]]

print(matrix_multiplying(matrix1, matrix2))
