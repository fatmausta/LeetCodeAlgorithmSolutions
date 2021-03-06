# LeetCode #382 Medium - Linked List Random Node

import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        pick = int(random.random() * len(self.range))
        return self.range[pick]

head = ListNode([[[1,2,3]],[]])
obj = Solution(head)
param_1 = obj.getRandom()