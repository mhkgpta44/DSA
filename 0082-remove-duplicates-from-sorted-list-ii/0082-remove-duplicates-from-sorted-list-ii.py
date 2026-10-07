class Solution:
    def deleteDuplicates(self, head):

        
        arr = []

        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        
        dummy = ListNode(0)
        tail = dummy

        for num in arr:
            if freq[num] == 1:
                tail.next = ListNode(num)
                tail = tail.next

        return dummy.next