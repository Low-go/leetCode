from typing import Optional
from linkedList import ListNode
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # Base cases
            if not list1:
                return list2
            if not list2:
                return list1


            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2


#obkects
list1 = ListNode(4)
list2 = ListNode(2, list1)
list3 = ListNode(1,list2)

#---

list4 = ListNode(4)
list5 = ListNode(3, list4)
list6 = ListNode(1,list5)


#output
solution = Solution()
result = solution.mergeTwoLists(list6, list3)
print(result)