'''
Two Sum
Solution
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Hint #1  
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you can come up with optimizations.


Hint #2  
So, if we fix one of the numbers, say
x
, we have to scan the entire array to find the next number
y
which is
value - x
where value is the input parameter. Can we change our array somehow so that this search becomes faster?

Hint #3  
The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

'''

from bisect import *
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myarr = []
        for i in range(len(nums)):
            myarr.append((nums[i], i))
        myarr.sort()
        
        nums = []
        mapping = []
        for e in myarr:
            nums.append(e[0])
            mapping.append(e[1])
        
        #right = bisect_right(nums, target)
        for i in range(len(nums)):
            e = nums[i]
            idx = bisect_left(nums, target-e, lo=i+1)
            if idx < len(nums) and nums[idx] == (target-e):
                return [mapping[i], mapping[idx]]
        return [-1, -1]
        