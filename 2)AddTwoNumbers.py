# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = ListNode() #dummy head placeholder
        current = newList 

        carry = 0
        while l1 or l2 or carry: #while all these are not null till theyre null
            v1 = l1.val if  l1 else 0 #0  takes care of edge case of number being too long
            v2 = l2.val if l2 else 0

            v3 = v1 + v2 + carry  #v3 is what we put into new list after customizing
            carry = v3 // 10
            value = v3 % 10
           

            current.next = ListNode(value) #insert into node new value
            
            #moving pointer for each list
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return newList.next
