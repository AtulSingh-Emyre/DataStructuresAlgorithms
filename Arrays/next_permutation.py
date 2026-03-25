# https://leetcode.com/problems/next-permutation/description/

"""
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
"""


class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        # print(i)
        if i >= 0:
            j = len(arr) - 1
            while j >= i and arr[j] <= arr[i]:
                j -= 1
            # print(j)
            self.swap(arr, i, j)
        self.reverse(arr, i + 1)

    def swap(self, arr: List[int], i: int, j: int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def reverse(self, arr: List[int], i: int):
        j = len(arr) - 1
        while i < j:
            self.swap(arr, i, j)
            i += 1
            j -= 1
