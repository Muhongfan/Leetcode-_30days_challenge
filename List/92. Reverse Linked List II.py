"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


1,2,3,4,5->

d, 1, 2, 3, 4, 5
  pre   cur_r
     left  right
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy

        if not head:
            return None

        # locate the first node
        for i in range(left - 1):
            pre = pre.next
        # print(pre)
        cur_r = pre

        for j in range(right - left):
            cur_r = cur_r.next

        left_flg = pre.next
        right_flg = cur_r

        next = right_flg.next
        left_flg, right_flg = self.reverseM(left_flg, right_flg, right_flg.next)
        # print(left_flg)
        # print(right_flg)

        pre.next = left_flg
        right_flg.next = next

        return dummy.next

    def reverseM(self, head, tail, terminal):
        cur = head
        # print(cur)
        prev = None
        while cur != terminal:
            remain = cur.next
            cur.next = prev
            prev = cur
            cur = remain
        print(head, tail)
        return tail, head

