#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = ListNode()
        pre = node
        node.next = head
        cur = head

        while cur:
            if cur.val != val:

                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                cur = cur.next
        return node.next