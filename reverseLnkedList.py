from linkedList import *
from typing import Optional
class Solution:


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            grab = head.next
            head.next = None
            return self.helper(head,grab)


    def helper(self, head: [ListNode],nextNode: [ListNode]):
        if (nextNode is None):
            return head
        else:
            hold = nextNode.next
            nextNode.next = head
            return self.helper(nextNode, hold)


