
def set_matrix_zeros(arr):
    c0 = 1
    R, C = len(arr), len(arr[0])
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 0:
                if c == 0:
                    c0 = 0
                else:
                    arr[0][c] = 0
                    arr[r][0] = 0
    for rr in arr:
        print(rr)
    print(c0)
    for r in range(1,R):
        for c in range(1,C):
            if arr[r][0] == 0 or arr[0][c] == 0:
                    print(f"{r},{c} cond2")
                    arr[r][c] = 0

    if c0 == 0:
        for r in range(R):
            arr[r][0] = 0
    if arr[0][0] == 0:
        for c in range(C):
            arr[0][c] = 0
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zeros(matrix)
for row in matrix:
    print(row)

