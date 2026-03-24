# https://leetcode.com/problems/maximum-subarray/

"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

We find the maximum sum of any subarray ending at position i. Then use it for processing i+1. Similar to DP approach.
Can be used as a reference for ideas.
"""

def get_max_subarray(arr: List[int]) -> int:
    max_sum = arr[0]
    curr_sum = 0
    for i in arr:
        curr_sum += i # Add current array element to curr_sum
        curr_sum = max(i, curr_sum) # See which is greater? [current value + max at previous index] OR [current value]
        max_sum = max(curr_sum, max_sum) # take the max of current sum
    return max_sum



