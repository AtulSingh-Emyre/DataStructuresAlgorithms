from Decorators.runtime_decorator import run_time_decorator

a = [2, 4, 7, 10]
b = [2, 3]

@run_time_decorator
def merge_sorted_array(a_arr, b_arr):
    c = []
    i,j = 0,0
    n,m = len(a_arr),len(b_arr)
    while i+j<n+m:
        if i == n:
            c.append(b_arr[j])
            j+=1
        elif j == m:
            c.append(a_arr[i])
            i+=1
        elif a_arr[i] < b_arr[j]:
            c.append(a_arr[i])
            i+=1
        else:
            c.append(b_arr[j])
            j+=1
    return c

print(merge_sorted_array(a, b))
