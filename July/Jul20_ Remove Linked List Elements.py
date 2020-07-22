"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    new_head = ListNode(0)
    #new_head = ListNode(None)
    #new_head = ListNode()
    new_head.next = head
    slow, fast = new_head, head
    while fast:
        if fast.val != val:
            slow.next.val = fast.val
            slow = slow.next
        fast = fast.next
    slow.next = None
    return new_head.next
#???????傻子pycharm
print(removeElements([1,2,6,3,4,5,6],6))


def removeElements2(head, val):
    dummy = ListNode(float('inf'))
    dummy.next = head
    previous, current = dummy, dummy.next
    while current:
        if current.val == val:
            previous.next = current.next
        else:
            previous = current
        current = current.next
    return dummy.next