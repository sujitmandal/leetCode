# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = temp = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            tempSum = temp1 + temp2 + carry
            
            temp.next = ListNode(tempSum % 10)
            temp = temp.next
            carry = tempSum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        print(head.next)
        return head.next


        
obj = Solution()
obj.addTwoNumbers([2,4,3], [5,6,4])

obj.addTwoNumbers([0], [0])
obj.addTwoNumbers( [9,9,9,9,9,9,9],[9,9,9,9])