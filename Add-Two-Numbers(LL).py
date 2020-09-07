# -*- coding: utf-8 -*-
"""
Add Two Numbers (linked lists)
"""

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        carry = 0
        head = l1
        while l2:
            _sum = l2.val + l1.val + carry
            l1.val = _sum % 10 #remainder
            carry = _sum // 10
            if l1.next is None:
                l1.next = l2.next #l1 is shorter than or equally as long as l2
                break
            if l2.next is None: #l2 is shorter than l1
                break
            l1 = l1.next
            l2 = l2.next
        while carry > 0:
            if l1.next is None:
                l1.next = ListNode(0)
            l1 = l1.next
            _sum = carry + l1.val
            l1.val = _sum % 10
            carry = _sum // 10

        return head
