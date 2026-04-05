problem_1 = [4, 3, 6, 2, 1, 1]

def missing_and_repeating(array):
    n = len(array)
    missing = -1
    repeating = -1
    for i in range(n):
        val = abs(array[i])
        if array[val-1] > 0:
            array[val-1] *= -1
        elif array[val-1] < 0:
            repeating  = val

    for i in range(n):
        if array[i] > 0:
            missing = i+1
    print(array)
    print(f"Missing and repeating values: {missing}, {repeating}")

missing_and_repeating(problem_1)
