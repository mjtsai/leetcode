#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math



class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        

        nl = [int(i) for i in str(n)]

        nlm = 1
        for i in nl:
            nlm = nlm*i
        nls = sum(nl)

        return nlm - nls


def main():
#{{{       

    sol = Solution()



    n1      = 234
    ans1    = 15

    sol1 = sol.subtractProductAndSum(n1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)


    #
    n2      = 4421
    ans2    = 21

    sol2 = sol.subtractProductAndSum(n2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)


#}}} 


      
if __name__ == "__main__":
    main()
