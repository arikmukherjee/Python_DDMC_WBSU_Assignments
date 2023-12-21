X = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Y = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
addition_result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
multiplication_result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        addition_result[i][j] = X[i][j] + Y[i][j]
        multiplication_result[i][j] = X[i][j] * Y[i][j]
print("Addition Result:")
for row in addition_result:
    print(row)
print("\nMultiplication Result:")
for row in multiplication_result:
    print(row)
