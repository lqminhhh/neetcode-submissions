# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        middle = len(stack) // 2
        
        for i in range(middle):
            temp = stack.pop()
            next_node = curr.next

            curr.next = temp
            temp.next = next_node

            curr = next_node

        curr.next = None
        return None