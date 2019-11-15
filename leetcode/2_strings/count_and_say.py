'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
   Hide Hint #1  
The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211
   Hide Hint #2  
To generate the nth term, just count and say the n-1th term.
'''

class Solution(object):
    def counts(self, arr):
        d = []
        c = arr[0]
        cc = 1
        i = 1
        while i < len(arr):
            if c == arr[i]:
                cc += 1
            else:
                d.append(cc)
                d.append(c)
                cc = 1
                c = arr[i]
            i += 1
        d.append(cc)
        d.append(c)
        return d;
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        prev = [1]
        terms = 1
        while terms < n:
            prev = self.counts(prev)
            terms += 1
        return "".join(map(lambda x: str(x), prev))
        