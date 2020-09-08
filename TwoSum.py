# -*- coding: utf-8 -*-
"""
Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

i.e
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = set()
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in numset):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
            numset.add(nums[i])