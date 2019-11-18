'''
Remove Nth Node From End of List
Solution
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

Hide Hint #1  
Maintain two pointers and update one with a delay of n steps.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(-1)
        root.next = head
        
        first = root
        k = 0
        while k < n+1 and first:
            first = first.next
            k += 1        
        second = root
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return root.next
