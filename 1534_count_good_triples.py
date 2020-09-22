#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
        gt = 0
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if( abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[k]-arr[i])<=c ):
                        gt += 1

        return gt

def main():
#{{{       

    sol = Solution()



    arr1    = [3,0,1,1,9,7]
    a1      = 7
    b1      = 2
    c1      = 3
    ans1    = 4

    sol1 = sol.countGoodTriplets(arr1, a1, b1, c1)

    print(ans1)
    assert(ans1 == sol1)


    #
    arr2    = [1,1,2,2,3]
    a2      = 0
    b2      = 0
    c2      = 1
    ans2    = 0

    sol2 = sol.countGoodTriplets(arr2, a2, b2, c2)

    print(ans2)
    assert(ans2 == sol2)



#}}} 


      
if __name__ == "__main__":
    main()
