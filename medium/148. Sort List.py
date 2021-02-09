# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        curr, length = head, 0
        while curr:
            curr, length = curr.next, length + 1

        root = ListNode(0)
        root.next = head
        intv = 1
        while intv < length:
            merge, curr = root, root.next
            while curr:
                h1, intv_1 = curr, intv
                while curr and intv_1:
                    curr, intv_1 = curr.next, intv_1 - 1
                if intv_1:
                    break

                h2, intv_2 = curr, intv
                while curr and intv_2:
                    curr, intv_2 = curr.next, intv_2 - 1

                len1, len2 = intv, intv - intv_2

                while len1 and len2:
                    if h1.val < h2.val:
                        merge.next, h1, len1 = h1, h1.next, len1 - 1
                    else:
                        merge.next, h2, len2 = h2, h2.next, len2 - 1
                    merge = merge.next
                if len1:
                    merge.next = h1
                else:
                    merge.next = h2
                while len1 > 0 or len2 > 0:
                    merge, len1, len2 = merge.next, len1 - 1, len2 - 1

                merge.next = curr
            intv *= 2

        return root.next
