# 链表的关键是非常精确地计算指针的位置，以及考虑None的末尾情况
class Solution(object):
    def isPalindrome(self, head):
        slow, fast, rev = head, head, None
        while fast and fast.next:
            rev, rev.next, slow, fast = slow, rev, slow.next, fast.next.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev
