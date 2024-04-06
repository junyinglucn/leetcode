# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        tmp = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            pre.next = tmp
            tmp = pre

        if fast:
            slow = slow.next

        while slow:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next

        return True
