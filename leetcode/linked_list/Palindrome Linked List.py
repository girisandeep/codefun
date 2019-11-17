'''
Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        st = []
        current = head
        while current:
            st.append(current.val)
            current = current.next
        
        current = head
        while current:
            if current.val != st.pop():
                return False
            current = current.next
        return True

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # Count Length
        l = 0
        current = head
        while current:
            l += 1
            current = current.next
        mid = l/2
        # print("mid", mid)
        
        # Skip "mid" num of nodes
        current = head
        skipped = 0
        while skipped < mid:
            skipped +=1 
            current = current.next
        firstend = current
        # print("firstend", firstend)
        if l%2 != 0:
            current = current.next
        
        # print("Second half", current)
        second = self.reverseList(current)
        # print("Reverse: ", second)
        
        first = head
        while first != firstend and second is not None:
            # print("Comparing first: ", first)
            # print("     with second: ", firstend)
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        
        prev = None
        current = head
        while current.next:
            first = current
            current = first.next
            first.next = prev
            prev = first
        current.next = prev
        return current