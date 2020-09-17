#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy



class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """

        assert(len(nums)>=1 and len(nums)<=100)
        assert(len(index)>=1 and len(index)<=100)
        for n in nums:
            assert(n>=0 and n<=100)
        for i in range(len(index)):
            assert(index[i]>=0 and index[i]<=i)

        ins = []

        for i in range(len(index)):
            ins.insert(index[i], nums[i])

        return ins


def main():
#{{{       

    sol = Solution()


    nums1   = [0,1,2,3,4]
    index1  = [0,1,2,2,1]
    ans1    = [0,4,1,3,2]

    sol1 = sol.createTargetArray(nums1, index1)

    print(ans1)
    assert(ans1 == sol1)

    #
    nums2   = [1,2,3,4,0]
    index2  = [0,1,2,3,0]
    ans2    = [0,1,2,3,4]

    sol2 = sol.createTargetArray(nums2, index2)

    print(ans2)
    assert(ans2 == sol2)

    #
    nums3   = [1]
    index3  = [0]
    ans3    = [1]

    sol3 = sol.createTargetArray(nums3, index3)

    print(ans3)
    assert(ans3 == sol3)

#}}} 


      
if __name__ == "__main__":
    main()
