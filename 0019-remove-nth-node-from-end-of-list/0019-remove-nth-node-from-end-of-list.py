# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        lent=0
        curr=head
        while curr:
            curr=curr.next
            lent+=1    
        pos=abs(lent-n)
        if pos==0:
            return head.next
        prev=None
        curr=head
        c=0
        while curr and c<pos:
            prev=curr
            curr=curr.next
            c+=1
        prev.next=curr.next
        return head    