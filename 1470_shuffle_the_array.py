#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        assert(n>=1 and n<=500)
        assert(len(nums) == 2*n)
        for i in range(len(nums)):    
            assert(nums[i]>=1 and nums[i] <= 10^3)

        lh = nums[0:n]
        rh = nums[n:2*n]

        m = []
        for i in range(n):
            m.append(lh.pop(0))   
            m.append(rh.pop(0))   

        return m

def main():
#{{{       

    sol = Solution()

    num1    = [2,5,1,3,4,7]
    n1      = 3
    ans1    = [2,3,5,4,1,7]

    sol1 = sol.shuffle(num1, n1)

    print(ans1)
    assert(ans1 == sol1)


    #
    num2    = [1,2,3,4,4,3,2,1]
    n2      = 4
    ans2    = [1,4,2,3,3,2,4,1]

    sol2 = sol.shuffle(num2, n2)

    print(ans2)
    assert(ans2 == sol2)


    #
    num3    = [1,1,2,2]
    n3      = 2
    ans3    = [1,2,1,2]

    sol3 = sol.shuffle(num3, n3)

    print(ans3)
    assert(ans3 == sol3)




#}}} 


      
if __name__ == "__main__":
    main()
