#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        ni_pairs = []
        for i in range(len(nums)):
            ni_pairs.append((nums[i], i))

        ni_pairs.sort(key=lambda x : x[0])

        smaller_nums = len(nums)*[0]
        for i in range(len(ni_pairs)):
            pos = ni_pairs[i][1]
            smi = i
            while(smi>=0):
                if(ni_pairs[smi][0] < ni_pairs[i][0]):
                    smaller_nums[pos] = smi+1
                    break
                smi -= 1

        return smaller_nums


def main():
#{{{       

    sol = Solution()




    nums0   = [8,1,2,2,3]
    ans0    = [4,0,1,1,3]

    sol0 = sol.smallerNumbersThanCurrent(nums0)

    print(ans0)
    print(sol0)
    assert(ans0 == sol0)


    #
    nums1   = [6,5,4,8]
    ans1    = [2,1,0,3]

    sol1 = sol.smallerNumbersThanCurrent(nums1)

    print(ans1)
    print(sol1)
    assert(ans1 == sol1)

    #
    nums2   = [7,7,7,7]
    ans2    = [0,0,0,0]

    sol2 = sol.smallerNumbersThanCurrent(nums2)

    print(ans2)
    print(sol2)
    assert(ans2 == sol2)

#}}} 


      
if __name__ == "__main__":
    main()
