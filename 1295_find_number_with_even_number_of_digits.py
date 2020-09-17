#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math


        
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        evn = 0

        for n in nums:
            if math.floor(math.log10(n)+1)%2 == 0:
                evn += 1

        return evn


def main():
#{{{       

    sol = Solution()



    nums1   = [12,345,2,6,7896]
    ans1    = 2

    sol1 = sol.findNumbers(nums1)

    print(ans1)
    assert(ans1 == sol1)


    #
    nums2   = [555,901,482,1771]
    ans2    = 1

    sol2 = sol.findNumbers(nums2)

    print(ans2)
    assert(ans2 == sol2)




#}}} 


      
if __name__ == "__main__":
    main()
