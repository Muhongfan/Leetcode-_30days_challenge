class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur_l = head
        cur_r = head

        if not head:
            return None
        while head:
            for i in range(0, left-1):
                pre = pre.next
                cur_l = cur_l.next
            for j in range(0, right-1):
                cur_r = cur_r.next

            next = cur_r.next
            left, right = self.reverseM(cur_l, cur_r, cur_r.next)
            pre.next = left
            right.next = next

        return dummy.next

    def reverseM(self, head, tail, terminal):
        cur = head
        pre = None
        while cur != terminal:
            remain = tail.next
            cur.next = pre
            pre = cur
            cur = remain
        return head, tail


So = Solution()
ans = So.reverseBetween([1,2,3,4,5],2,4)
print(ans)