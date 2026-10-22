# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        middle=slow
        curr=middle.next
        middle.next=None
        prev=None
        while curr:
            node=curr.next
            curr.next=prev
            prev=curr
            curr=node 
        trail=prev
        lead=head
        while trail:
            front=lead.next
            lead.next=trail
            lead=front
            back=trail.next
            trail.next=lead
            trail=back