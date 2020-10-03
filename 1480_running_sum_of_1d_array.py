#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        rs = [0]
    
        for i in range(len(nums)):
            rs.append(rs[-1]+nums[i])

        return rs[1:]


def main():
#{{{       

    sol = Solution()



    nums1   = [1,2,3,4]
    ans1    = [1,3,6,10]

    sol1 = sol.runningSum(nums1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)


    #

    nums2   = [1,1,1,1,1]
    ans2    = [1,2,3,4,5]

    sol2 = sol.runningSum(nums2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)


#}}} 


      
if __name__ == "__main__":
    main()
