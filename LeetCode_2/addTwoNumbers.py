#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 11:23
# @Author  : H
# @File    : addTwoNumbers.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l: list) -> ListNode:
    print("[ ", end="")
    while l:
        print("%d  " % (l.val), end="")
        l = l.next
    print("]", end="")


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        flag = 0
        while l1 or l2:
            if l1:
                if l2:
                    result.append((l1.val + l2.val + flag) % 10)
                    if l1.val + l2.val + flag > 9:
                        flag = 1
                    else:
                        flag = 0
                    l1 = l1.next
                    l2 = l2.next
                else:
                    result.append((l1.val + flag) % 10)
                    if l1.val + flag > 9:
                        flag = 1
                    else:
                        flag = 0
                    l1 = l1.next
            else:
                if l2:
                    result.append((l2.val + flag) % 10)
                    if l2.val + flag > 9:
                        flag = 1
                    else:
                        flag = 0
                    l2 = l2.next
                else:
                    break
        if flag > 0: result.append(flag)
        return generateList(result)


if __name__ == '__main__':
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    l1 = generateList(l1)
    l2 = generateList(l2)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    printList(result)
