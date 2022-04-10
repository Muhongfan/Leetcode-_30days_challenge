"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p1 = head
        p2 = head.next
        p1.next = self.swapPairs(p2.next)
        p2.next = p1
        return p2

    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head and head.next:
            cur = head
            cur_next = cur.next

            prev.next = cur_next
            cur.next = cur_next.next
            cur_next.next = cur

            prev = cur
            head = cur.next
        return dummy.next







