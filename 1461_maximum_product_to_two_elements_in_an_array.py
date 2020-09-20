#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy




class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        assert(len(nums)>=2 and len(nums)<=500)
        for n in nums:
            assert(n>=1 and n<=10^3)

        
#        for i in range(len(nums)):
#            nums[i] -= 1;

        mxi = nums.index(max(nums))
        nums[-1], nums[mxi] = nums[mxi], nums[-1]
        mx = max(nums[0:-1])

        return (nums[-1]-1)*(mx-1)





        


def main():
#{{{       

    sol = Solution()

    nums1   = [3,4,5,2]
    ans1    = 12
    sol1 = sol.maxProduct(nums1)

    print(ans1)
    print(sol1)
    assert(ans1 == sol1)


    #
    nums2   = [1,5,4,5]
    ans2    = 16
    sol2 = sol.maxProduct(nums2)

    print(ans2)
    print(sol2)
    assert(ans2 == sol2)





#}}} 


      
if __name__ == "__main__":
    main()
