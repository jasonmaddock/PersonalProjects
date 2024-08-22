class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val or list1.val == list2.val:
            return ListNode(list2.val, self.mergeTwoLists(self, list1, list2.next))
        else:
            return ListNode(list1.val, self.mergeTwoLists(self, list1.next, list2))

        