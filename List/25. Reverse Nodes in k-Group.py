"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""

#时间复杂度: O(n)
#空间复杂度: O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverse(self, head, tail, terminal):
        #reverse
        cur = head
        pre = None
        while cur != terminal:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return head, trail
    def reverseKgroup(self, head, k):
        # visual node
        ans = Listnode()
        ans.next = head
        pre = ans
        # when the link not end
        while head:
            #init trail and set it in the k step
            tail = head
            for i in range(k-1):
                tail = tail.next
                # if to the end, print the whole link list
                if not tail: # if tail == None:
                    return ans.next
            # add the sub to the original link
            pre.next = head
            tail.next = next
            pre = tail
            head = tail.next
        # print the whole
        return ans.head





