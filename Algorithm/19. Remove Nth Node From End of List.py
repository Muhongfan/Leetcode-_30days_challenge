"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head.next is None:
            return None
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        if n == 1:
            slow.next = None
        else:
            slow.next = slow.next.next
        return head

    #无边界判断
    # one pointer jump to n step and updated the pointer and the other one as the same step
    def removeNthFromEnd2(self, head, n):

        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head

        i = 0
        while fast.next is not None and i != n:
            fast = fast.next
            i += 1

        while fast and fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = head, head

        i = 1
        while curr.next is not None:
            curr = curr.next
            if i > n:
                prev = prev.next

            i += 1

        if i == n:
            return head.next

        prev.next = prev.next.next
        return head