#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if __name__ == "__main__":
        if isinstance(matrix, list):
            new_matrix = []
            for i in range(len(matrix)):
                row =[]
                for j in range(len(matrix[i])):
                    row.append(matrix[i][j]**2)
                new_matrix.append(row)
        return new_matrix






matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
