#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy



class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert(len(nums)>=1 and len(nums) <= 100)
        for i in range(len(nums)):    
            assert(nums[i]>=1 and nums[i] <= 100)


        # find same value set
        val_cnt = {}
        for i in range(len(nums)):
            if(nums[i] not in val_cnt.keys()):
                val_cnt[nums[i]] = 1
            else:
                val_cnt[nums[i]] +=1

        #
        tot = 0
        for k, v in val_cnt.items():
            tot += sum(range(v))

        return tot

        


def main():
#{{{       

    sol = Solution()

    num1    = [1,2,3,1,1,3]
    ans1    = 4

    sol1 = sol.numIdenticalPairs(num1)

    print(ans1)
    print(sol1)
    assert(ans1 == sol1)


    #
    num2    = [1,1,1,1]
    ans2    = 6

    sol2 = sol.numIdenticalPairs(num2)

    print(ans2)
    print(sol2)
    assert(ans2 == sol2)

    #
    num3    = [1,2,3]
    ans3    = 0

    sol3 = sol.numIdenticalPairs(num3)

    print(ans3)
    print(sol3)
    assert(ans3 == sol3)





#}}} 


      
if __name__ == "__main__":
    main()
