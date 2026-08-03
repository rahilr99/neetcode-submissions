# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            current=head
            stack=[]
            stack.append(current)
            while(current is not None):
                current=current.next
                if(current is not None):
                    stack.append(current)
            if stack:
                head=stack.pop()
                current=head        
            while stack:
                current.next=stack.pop()
                current=current.next
            current.next=None
        return head
            


