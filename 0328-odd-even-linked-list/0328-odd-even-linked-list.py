# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head==None or head.next==None:
            return head
        # odd=head
        # even=head.next
        # temp=head.next
        # while even!=None and even.next!=None:
        #     odd.next=even.next
        #     odd=odd.next
        #     even.next=odd.next
        #     even=even.next
        # odd.next=temp
        # return head
        odd=[]
        even=[]
        curr=head
        pos=1
        while curr:
            if pos%2==1:
                odd.append(curr)
            else:
                even.append(curr)
            curr=curr.next  
            pos+=1
        for i in range(len(odd)-1):
            odd[i].next=odd[i+1]
        for j in range(len(even)-1):
            even[j].next=even[j+1]
        odd[len(odd)-1].next=even[0]
        even[len(even)-1].next=None
        return head
