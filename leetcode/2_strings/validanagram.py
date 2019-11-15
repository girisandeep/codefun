'''
Valid Anagram
Solution
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        d = [0]*26
        a = ord('a')
        for k in s:
            d[ord(k) - a] += 1
            
        for k in t:
            d[ord(k) - a] -= 1
        for e in d:
            if e != 0:
                return False
        return True

class Solution2(object):
    def getcounts(self, s):
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        return d
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = self.getcounts(s)
        d2 = self.getcounts(t)
        for k, v in d1.items():
            if k in d2 and d2[k] == v:
                del d2[k]
            else:
                return False
        return len(d2) == 0
    
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    