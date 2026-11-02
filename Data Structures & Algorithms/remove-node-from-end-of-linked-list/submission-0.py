# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        cnt = 0
        # count the total length of the list
        while curr:
            cnt += 1
            curr = curr.next

        curr = head
        start = cnt - n - 1

        # if nth node is the start of the linked list
        if start < 0:
            return head.next        

        # traverse until n - 1 node
        while start > 0:
            start -= 1
            curr = curr.next

        # remove nth node
        temp = curr.next
        curr.next = temp.next if temp else None
        return head

"""
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7; n = 3

"""