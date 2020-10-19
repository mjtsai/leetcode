#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
       
        step = 0

        for i in range(0, len(points)-1):
            h = abs(points[i][0] - points[i+1][0])
            v = abs(points[i][1] - points[i+1][1])
            mn = min(h, v)
            mx = max(h, v)
            s = mx-mn

            step = step + mn + s

        return step



def main():
#{{{       

    sol = Solution()



    points1 = [[1,1],[3,4],[-1,0]]
    ans1    = 7

    sol1 = sol.minTimeToVisitAllPoints(points1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)


#
    points2 = [[3,2],[-2,2]]
    ans2    = 5

    sol2 = sol.minTimeToVisitAllPoints(points2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)


    

#}}} 


      
if __name__ == "__main__":
    main()
