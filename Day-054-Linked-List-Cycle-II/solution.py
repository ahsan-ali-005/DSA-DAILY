# Definition for singly-linked list.
from typing_extensions import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fast, slow = head, head

        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break

        fast = head
        
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast