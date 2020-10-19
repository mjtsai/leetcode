#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math

class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        
        mat = [ [0]*m for _ in range(n) ]
        for (i, j) in indices:
            for i_m in range(m):
                mat[i][i_m]+=1
            for i_n in range(n):
                mat[i_n][j]+=1
            

        odd_cnt = 0
        for i_m in range(m):
            for i_n in range(n):
                if(mat[i_n][i_m]%2):
                    odd_cnt+=1

        return odd_cnt


def main():
#{{{       

    sol = Solution()



    n1          = 2
    m1          = 3
    indices1    = [[0,1],[1,1]]
    ans1        = 6

    sol1 = sol.oddCells(n1, m1, indices1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)

#

    n2          = 2
    m2          = 2
    indices2    = [[1,1],[0,0]]
    ans2        = 0

    sol2 = sol.oddCells(n2, m2, indices2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)


    

#}}} 


      
if __name__ == "__main__":
    main()
