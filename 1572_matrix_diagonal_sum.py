#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math



class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """


        sz = len(mat)

        summ = 0
        for i in range(sz):
            summ += mat[i][i]
            summ += mat[i][sz-1-i]

        if(sz%2==1):
            summ -= mat[int(sz/2)][int(sz/2)]

        return summ




def main():
#{{{       

    sol = Solution()



    mat1    = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    ans1    = 25

    sol1 = sol.diagonalSum(mat1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)


    #
    mat2    = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
    ans2    = 8

    sol2 = sol.diagonalSum(mat2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)


    #
    mat3    = [[5]]
    ans3    = 5

    sol3 = sol.diagonalSum(mat3)

    print(sol3)
    print(ans3)
    assert(ans3 == sol3)


#}}} 


      
if __name__ == "__main__":
    main()
