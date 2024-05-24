# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head: ListNode):
            rev = ListNode()
            tail = head
            while tail:
                rev.next = ListNode(tail.val)
                rev = rev.next
                tail = tail.next

            prev, curr = None, rev.next 
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt 
            return prev
        rev = reverse(head)

        while head:
            print(head.val, rev.val)
            if head.val != rev.val:
                return False
            head, rev = head.next, rev.next

        print(head.val, rev.val)
        return True
    

    
def create_list(arr: List[int]) -> ListNode:
    head = ListNode()
    tail = head
    for n in arr:
        tail.next = ListNode(n)
        tail = tail.next
    return head.next
    
if __name__ == "__main__":
    s = Solution()
    head = create_list([1,1,2,1])
    print(s.isPalindrome(head))