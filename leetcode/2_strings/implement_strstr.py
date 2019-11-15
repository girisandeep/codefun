'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

'''
# 
# bad - better than 89%
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ln = len(needle)
        lh = len(haystack)
        if ln == 0:
            return 0
        if lh == 0:
            return -1
        i = 0
        for i in range(lh):
            if lh - i < ln:
                return -1
            j = 0
            while j < ln:
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == ln:
                return i
        return -1

# Better than 20%
class Solution(object):
    def startswith(self, haystack, start, needle):
        lh = len(haystack) - start 
        ln = len(needle)
        if lh < ln:
            return False
        
        j = 0
        while j < ln:
            if needle[j] != haystack[start+j]:
                return False
            j += 1
        return True
    
            
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        print("Searching for ", needle, ' in ', haystack)
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        i = 0
        j = 0
        found = -1
        for i in range(len(haystack)):
            if self.startswith(haystack, i, needle):
                return i
            i += 1
        
        return -1