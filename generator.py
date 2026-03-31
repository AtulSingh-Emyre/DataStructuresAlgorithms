import sys

"""
Effectively used for iterating larger datasets. 
Generator is a tool in python that enables us to produce a sequence of values.
They are great for reading large files line by line without loading the entire file into memory.
"""

# 1. Returning a List (Eager Evaluation)
def get_data_list(n=50):
    res = []
    for i in range(n):
        res.append(i)
    return res
# 2. Yielding a Generator (Lazy Evaluation)
def get_data_generator(n=50):
    for i in range(n):
        yield i

# Memory Test (1 million items)
big_list = get_data_list(10**6)
big_gen = get_data_generator(10**6)

print(f"List size: {sys.getsizeof(big_list)} bytes")  # ~8 MB
print(f"Generator size: {sys.getsizeof(big_gen)} bytes")  # ~100 bytes