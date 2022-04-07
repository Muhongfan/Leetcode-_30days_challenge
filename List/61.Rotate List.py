class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head ==None:
            return None
        count = 0
        p1 = head
        while p1:
            count += 1
            p1 = p1.next
        p1 = head
        p2 = head
        k = k%count
        while k:
            k = k-1
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = head
        head = p1.next
        p1.next = None
        return head


