#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        

        assert(len(candies)>=2 and len(candies)<=100)
        for c in candies:
            assert(c>=1 and c<=100)
        assert(extraCandies>=1 and extraCandies<=50)



        mx = max(candies)
        gst = len(candies)*[None]

        for i in range(len(candies)):
            if candies[i]+extraCandies >= mx:
                gst[i] = True
            else:
                gst[i] = False

        return gst
        


def main():
#{{{       

    sol = Solution()



    candies1        = [2,3,5,1,3]
    extraCandies1   = 3
    ans1            = [True,True,True,False,True]

    sol1 = sol.kidsWithCandies(candies1, extraCandies1)

    print(ans1)
    assert(ans1 == sol1)

    #
    candies2        = [4,2,1,1,2]
    extraCandies2   = 1
    ans2            = [True,False,False,False,False]

    sol2 = sol.kidsWithCandies(candies2, extraCandies2)

    print(ans2)
    assert(ans2 == sol2)


    #
    candies3        = [12,1,12]
    extraCandies3   = 10
    ans3            = [True,False,True]

    sol3 = sol.kidsWithCandies(candies3, extraCandies3)

    print(ans3)
    assert(ans3 == sol3)





#}}} 


      
if __name__ == "__main__":
    main()
