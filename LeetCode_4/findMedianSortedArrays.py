#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 17:54
# @Author  : H
# @File    : findMedianSortedArrays.py
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        counts, flag = divmod(len(nums1) + len(nums2) + 1, 2)
        print(counts,flag)
        counts = counts + flag
        print(counts)
        result = 0
        while counts:
            counts -= 1
            if nums1 and nums2:
                min_p = nums1.pop() if nums1[-1] > nums2[-1] else nums2.pop()
            elif nums1 and not nums2:
                min_p = nums1.pop()
            elif nums2 and not nums1:
                min_p = nums2.pop()
            if flag == 1 and counts < 2:
                result = (result + min_p)
        result = result / 2 if flag == 1 else min_p
        return result


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
