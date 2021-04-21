#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 10:35
# @Author  : H
# @File    : twoSum.py
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            for sec in range(first + 1, len(nums)):
                if target == nums[first] + nums[sec]:
                    return [first, sec]
                else:
                    continue


if __name__ == '__main__':
    nums = [-1, -2, -3, -4, -5]
    target = -8
    soutltion = Solution()
    print(soutltion.twoSum(nums, target))
