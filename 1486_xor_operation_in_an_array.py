#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy



class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        assert(n>=1 and n<=1000)
        assert(start>=0 and start<=1000)

        xor = 0
        
        for i in range(n):
            num_i = start+2*i
            xor = xor ^ num_i

        return xor



def main():
#{{{       

    sol = Solution()



    n1      = 5
    start1  = 0
    ans1    = 8

    sol1 = sol.xorOperation(n1, start1)

    print(ans1)
    assert(ans1 == sol1)


    #
    n2      = 4
    start2  = 3
    ans2    = 8

    sol2 = sol.xorOperation(n2, start2)

    print(ans2)
    assert(ans2 == sol2)

    #
    n3      = 1
    start3  = 7
    ans3    = 7

    sol3 = sol.xorOperation(n3, start3)

    print(ans3)
    assert(ans3 == sol3)

    #
    n4      = 10
    start4  = 5
    ans4    = 2

    sol4 = sol.xorOperation(n4, start4)

    print(ans4)
    assert(ans4 == sol4)


#}}} 


      
if __name__ == "__main__":
    main()
