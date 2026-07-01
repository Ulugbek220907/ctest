"""

this algo is for the leetcode problem "add two numbers"
given two linked lists, each representing a non-negative integer in reverse order
add the two numbers and return the sum as a linked list.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        number1, number2 = 0, 0
        current1, current2 = l1, l2

        i, k = 0, 0
        while current1:
            number1 = number1 + current1.val * (10 ** i)
            current1 = current1.next
            i += 1
        

        while current2:
            number2 = number2 + current2.val * (10 ** k)
            current2 = current2.next
            k += 1
        
        result = number1 + number2
        result_str = str(result)

        # Create a new linked list for the result
        dummy_head = ListNode(0)
        current = dummy_head
        for digit in reversed(result_str):
            current.next = ListNode(int(digit))
            current = current.next

        return dummy_head.next