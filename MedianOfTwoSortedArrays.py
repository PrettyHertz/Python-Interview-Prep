# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:45:41 2020

@author: miked
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        while len(nums2) != 0:
            if (i < len(nums1)):
                if (nums2[0] <= nums1[i]):
                    nums1.insert(i,nums2[0])
                    del nums2[0]
                else:
                    i += 1 #move over one index in nums1
            else:
                nums1.extend(nums2) #append rest of second list to first
                del nums2[0:]
        if (len(nums1)%2):
            return nums1[len(nums1)//2]
        else:
            return(((nums1[len(nums1)//2])+(nums1[len(nums1)//2-1]))/2)
                