# -*- coding: utf-8 -*-
"""
Find longest substring in a given string
"""

class Solution:
    def lengthOfLongestSubstring(self, string):

        maxL = 0
        tail, headd = 0, 0
        chars = set()
        while tail < len(string) and headd < len(string):
            if string[headd] not in chars:
                chars.add(string[headd])
                headd += 1
                maxL = max(maxL, headd - tail)
            else:
                chars.remove(string[tail])
                tail += 1
        return maxL
                