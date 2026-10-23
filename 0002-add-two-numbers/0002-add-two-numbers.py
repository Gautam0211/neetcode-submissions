# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # curr=None
        # head=None
        dummy=ListNode(0)
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            total=carry
            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            digit=total%10
            carry=total//10
            # new_node=ListNode(digit)
            # if head==None:
            #     head=new_node
            #     curr=new_node         
            # else:
            curr.next=ListNode(digit)
            curr=curr.next
        # return head   
        return dummy.next     