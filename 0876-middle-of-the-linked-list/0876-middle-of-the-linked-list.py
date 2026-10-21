# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        curr=head
        c=0
        while curr is not None:
            curr=curr.next
            c+=1
        total_nodes=c
        curr=head
        tar_node=total_nodes//2
        p=0
        while p<tar_node:
            curr=curr.next
            p+=1
        return curr        
