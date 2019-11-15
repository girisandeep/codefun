'''
First Unique Character in a String
Solution
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i,c in enumerate(s):
            if c in d:
                d[c] = -1
            else:
                d[c] = i
        for v in sorted(d.values()):
            if v != -1:
                return v
        return -1

# This was supposed to be faster but itseems it is slow
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # -2 - Does not exist
        # -1 - repeated
        # 0 or above - not repeated and is the index
        d = [-2]*26
        
        a = ord('a')
        for i,c in enumerate(s):
            v = ord(c) - a
            if d[v] == -2:
                d[v] = i
            elif d[v] > -1:
                d[v] = -1

        minidx = len(s)
        for idx in d:
            if idx > -1 and idx < minidx:
                minidx = idx
        if minidx == len(s):
            return -1
        return minidx
