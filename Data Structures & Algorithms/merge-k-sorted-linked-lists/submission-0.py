# Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:  
    def linkedListToDeque(self, ll_list):
        listOfAllVals = deque()
        for ll in ll_list:
            while ll:
                listOfAllVals.append(ll.val)
                ll=ll.next
        return listOfAllVals

    def dequeToLinkedList(self, dqlist):
        head, prev, current = None, None, None
        for val in dqlist: 
            if not head: 
                head = ListNode(val = val)
                prev = head
            else: 
                current = ListNode(val = val)
                prev.next = current
                prev = current
        return head
    
    def merge_sort(self, arr, start, end):
        if start == end:
            return deque([arr[start]])
    
        mid = (start + end) // 2
        left = self.merge_sort(arr, start, mid)
        right = self.merge_sort(arr, mid + 1, end)
        return self.merge(left, right)

    def merge(self, left, right):
        sorted_list = deque()
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                sorted_list.append(left[l])
                l += 1
            else:
                sorted_list.append(right[r])
                r += 1
        while l < len(left):
            sorted_list.append(left[l])
            l += 1
        while r < len(right):
            sorted_list.append(right[r])
            r += 1
        return sorted_list

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
    
        dq_list = self.linkedListToDeque(lists)
        if not dq_list:
            return None
    
        sorted_vals = self.merge_sort(list(dq_list), 0, len(dq_list) - 1)
        return self.dequeToLinkedList(sorted_vals)


    
