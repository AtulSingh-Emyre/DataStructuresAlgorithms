from Decorators.runtime_decorator import void_runtime_decorator

problem_1 = [0, 1, 2, 0, 1, 2]*10000
problem_2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

@void_runtime_decorator
def dutch_national_flag_solver(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            swap(arr,low,mid)
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            swap(arr,mid,high)
            high -= 1

dutch_national_flag_solver(problem_1)
print(problem_1)

dutch_national_flag_solver(problem_2)
print(problem_2)