#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math


class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       

        derle = []
        for i in range(0, len(nums), 2):
            derle.extend(nums[i]*[nums[i+1]])

        return derle



def main():
#{{{       

    sol = Solution()



    nums1   = [1,2,3,4]
    ans1    = [2,4,4,4]

    sol1 = sol.decompressRLElist(nums1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)


    #
    nums2   = [1,1,2,3]
    ans2    = [1,3,3]

    sol2 = sol.decompressRLElist(nums2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)



#}}} 


      
if __name__ == "__main__":
    main()
