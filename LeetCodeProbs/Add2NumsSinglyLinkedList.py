# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#    self.head = None
#    self.size = 0

#    def insertStart(self, val=0):

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rl = ListNode()
        carry = 0
        while l1 or l2 or carry:
            rl.val = (l1.val + l2.val + carry)%10
            carry = (l1.val + l2.val)//10
            l1 = l1.next
            l2 = l2.next
            rl = rl.next
        return rl

def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    while l1 and l1.val != 0:
        print(l1.val)
        l1 = l1.next

if __name__=='__main__':
    main()