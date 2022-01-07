"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # creating two pointers to store the first node as prev and the next node as curr
        curr = head.next
        prev = head

        while(curr):
            if curr.val == prev.val:
            # increment the pointer to point to the next node if the values are same
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
