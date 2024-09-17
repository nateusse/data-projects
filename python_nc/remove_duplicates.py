"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once.
 The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, 
to get accepted, you need to do the following things:

    Change the array nums such that the first k elements 
    of nums contain the unique elements in the order they were present in nums initially.
      The remaining elements of nums are not important as well as the size of nums.
    Return k.

"""

class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        L = 1
        
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
        return L

# Create an instance of the Solution class
solution = Solution()

# Define the list
lista = [1, 1, 2]

# Call the removeDuplicates method on the instance and print the result
print(solution.remove_duplicates(lista))  # Output should be 2