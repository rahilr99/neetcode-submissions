# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''if head is not None:
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
        return head'''
        if head:
            current=head
            new_next=None
            next_forward=head.next
            while current:
                current.next=new_next
                new_next=current
                current=next_forward
                if current:
                    next_forward=next_forward.next
            head=new_next
        return head


            


