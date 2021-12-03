"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        new1, new2 = ListNode(), ListNode()
        cur1, cur2, cur = new1, new2, head

        while cur:
            if cur.val >= x:
                cur1.next = cur
                cur1 = cur1.next

            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        cur2.next = new1.next
        # cut the link between the final larger point to its original next
        cur1.next = None

        return new2.next