#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        n_neighbors_le_0 = 4
        dist_contour = 1

        value_change = True
        while(value_change):
            value_change = False

            for row in range(0, len(matrix)):
                for col in range(0, len(matrix[row])):
                    if(matrix[row][col]<=0):
                        continue
                    neighbors = []
                    if row-1>=0 : neighbors.append(matrix[row-1][col])
                    if col-1>=0 : neighbors.append(matrix[row][col-1])
                    if row+1<len(matrix) : neighbors.append(matrix[row+1][col])
                    if col+1<len(matrix[row]) : neighbors.append(matrix[row][col+1])

                    neighbors = [n for n in neighbors if (-n+1) == dist_contour]
                    if(len(neighbors)):
                        dist = -dist_contour
                        if(dist != matrix[row][col]):
                            value_change = True
                            matrix[row][col] = dist

            #
            dist_contour = dist_contour+1

        #
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                assert(matrix[row][col]<=0)
                matrix[row][col] = -matrix[row][col]
        
        return matrix




def main():
#{{{       

    sol = Solution()


    mat1    =  [[0,0,0],
                [0,1,0],
                [0,0,0]]
    ans1    =  [[0,0,0],
                [0,1,0],
                [0,0,0]]

    sol1 = sol.updateMatrix(mat1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)


    #
    mat2    =  [[0,0,0],
                [0,1,0],
                [1,1,1]]
    ans2    =  [[0,0,0],
                [0,1,0],
                [1,2,1]]

    sol2 = sol.updateMatrix(mat2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)


    # wrong answer
    mat3    =  [[1,0,1,1,0,0,1,0,0,1],
                [0,1,1,0,1,0,1,0,1,1],
                [0,0,1,0,1,0,0,1,0,0],
                [1,0,1,0,1,1,1,1,1,1],
                [0,1,0,1,1,0,0,0,0,1],
                [0,0,1,0,1,1,1,0,1,0],
                [0,1,0,1,0,1,0,0,1,1],
                [1,0,0,0,1,1,1,1,0,1],
                [1,1,1,1,1,1,1,0,1,0],
                [1,1,1,1,0,1,0,0,1,1]] 

#    ans3    =  [[1,0,1,1,0,0,1,0,0,1],
#                [0,1,1,0,1,0,1,0,1,1],
#                [0,0,1,0,1,0,0,1,0,0],
#                [1,0,1,0,1,1,1,1,1,1],
#                [0,1,0,1,1,0,0,0,0,1],
#                [0,0,1,0,1,1,1,0,1,0],
#                [0,1,0,1,0,1,0,0,1,1],
#                [1,0,0,0,1,2,1,1,0,1],
#                [2,1,1,1,1,2,1,0,1,0],
#                [2,2,2,1,0,1,0,0,1,1]]
    ans3    =  [[1,0,1,1,0,0,1,0,0,1],
                [0,1,1,0,1,0,1,0,1,1],
                [0,0,1,0,1,0,0,1,0,0],
                [1,0,1,0,1,1,1,1,1,1],
                [0,1,0,1,1,0,0,0,0,1],
                [0,0,1,0,1,1,1,0,1,0],
                [0,1,0,1,0,1,0,0,1,1],
                [1,0,0,0,1,2,1,1,0,1],
                [2,1,1,1,1,2,1,0,1,0],
                [3,2,2,1,0,1,0,0,1,1]]

    sol3 = sol.updateMatrix(mat3)

    print(sol3)
    print(ans3)
    assert(ans3 == sol3)

#}}} 


      
if __name__ == "__main__":
    main()
