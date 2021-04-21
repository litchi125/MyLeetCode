#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 15:06
# @Author  : H
# @File    : lengthOfLongestSubstring.py


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        window = []  # 窗口
        max_legth = 0  # 记录窗口最大长度
        for i in s:
            if i not in window:
                window.append(i)  # 若当前位置的值不在窗口内，则追加
            else:
                window = window[window.index(i) + 1:]  # 若当前位置的值在窗口内，则删除窗口内当前值所在索引及之前的值，
                # 保留其余值
                window.append(i)  # 追加当前位置的值到窗口
            if len(window) > max_legth:
                max_legth = len(window)  # 记录最大窗口长度
        return max_legth


if __name__ == '__main__':
    string = "aabaab!bb"
    soulution = Solution()
    print(soulution.lengthOfLongestSubstring(string))
