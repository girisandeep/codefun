'''
Reverse Integer
Solution
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        is_neg = False
        if x < 0:
            x = -x
            is_neg = True
        max_int = 2**31-1
        min_int = -2**31
        while x > 0:
            result = result * 10 + x%10
            if result > max_int:
                return 0
            x = x/10
        if is_neg:
            return -result
        return result
