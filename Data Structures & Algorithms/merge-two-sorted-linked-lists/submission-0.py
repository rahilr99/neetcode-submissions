# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev_node = None

        current_l1 = list1
        current_l2 = list2

        while current_l1 or current_l2: 
            if current_l1 and current_l2:
                if current_l1.val <= current_l2.val:
                    current = ListNode(val=current_l1.val)
                    current_l1 = current_l1.next
                else:
                    current = ListNode(val=current_l2.val)
                    current_l2 = current_l2.next   
            elif current_l1:    
                current = ListNode(val=current_l1.val)
                current_l1 = current_l1.next
            else:  # current_l2 must be non-empty
                current = ListNode(val=current_l2.val)
                current_l2 = current_l2.next

            if not head:
                head = current
                prev_node = current
            else:
                prev_node.next = current
                prev_node = current

        return head
