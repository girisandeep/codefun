'''
Distribute Candies
https://leetcode.com/problems/distribute-candies/

Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.
Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 
Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
'''

# Solution

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # Compute frequencies
        freq = {}
        for c in candies:
            freq[c] = freq.get(c, 0) + 1
        
        each_gets = len(candies)/2
        uniq = len(freq.keys())
        
        # Best case scenerio
        if uniq <= each_gets:
            return uniq
        elif uniq > each_gets:
            # If sister picked one from each variety, the brother will be left with b
            b = sum(map(lambda x:x - 1, freq.values()))
            return uniq - (each_gets - b)

def main():
    s = Solution()
    print(s.distributeCandies([1,1,2,2,3,3]))
    print(s.distributeCandies([11,22,3,4, 5, 6]))
        
if __name__ == '__main__':
    main()