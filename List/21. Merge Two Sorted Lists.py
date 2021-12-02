"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Input: list1 = [], list2 = []
Output: []
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # assume a new list with a head
        head = ListNode()
        cur = head
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                # l1 should continue
                l1 = l1.next
            else:
                cur.next = l2
                # l2 should continue
                l2=l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        # should start with the second point of the new list
        return head.next