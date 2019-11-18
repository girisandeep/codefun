'''
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = ListNode(-1)
        root = current
        while l1 and l2:
            vl1 = l1.val
            vl2 = l2.val
            if vl1 < vl2:
                smaller = l1
                l1 = l1.next
            else:
                smaller = l2
                l2 = l2.next
            current.next = smaller
            current = smaller
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        return root.next