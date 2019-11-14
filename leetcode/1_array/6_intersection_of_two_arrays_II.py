'''
Intersection of Two Arrays II
Solution
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

from bisect import *
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        if len(nums1) > len(nums2):
            needle = nums2
            hay = nums1
        else:
            needle = nums1
            hay = nums2
        lo = 0
        high = len(hay)-1
        result = []
        prev = None
        prev_result = None
        for x in needle:
            print("Searching ", x, prev_result)
            if lo > high:
                break
            idx = bisect_left(hay,x,lo=lo)
            print("idx: ", idx)
            if idx > high:
                break;
            elif hay[idx] == x:
                result.append(x)
                lo = idx+1
            else:
                lo = idx
        return result
