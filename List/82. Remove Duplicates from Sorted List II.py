"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""

"""
d 1,2,3,3,4,4,5
^ ^
p c
if cur is not eaqual to cur.next, which means p and c should both move to the next

d 1,2,3,3,4,4,5
  ^ ^
  p c
if cur is not equal to cur.next, which means p and c should both move to the next

d 1,2,3,3,4,4,5
    ^ ^
    p c
cur is equal to cur.next, p keeps and c move to the next

d 1,2,3,3,4,4,5
    ^   ^
    p   c
since cur and cur.next is not equal, p.next = cur.next

d 1,2,\3,\3,4,4,5
    ^     ^
    p     c
    
 d 1,2,4,4,5
     ^ ^
     p c   
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
        d = ListNode()
        d.next = head
        pre = d
        cur = head
        while cur and cur.next:
            while cur.val == cur.next.val:
                cur = cur.next
            #if cur.val != cur.next.val:  -> 无法判断[1,1,2,3] 错误返回[1,2,3]
            #while cur.val != cur.next.val:  -> 无判断cur.next是否存在，无法判断[1,1]

            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return d.next



