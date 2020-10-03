#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stk = []
        bss = 0
        for i in range(len(s)):
            if(len(stk)==0):
                stk.append(s[i])
            elif(stk[-1] != s[i]):
                stk.pop()
            else:
                stk.append(s[i])

            if(len(stk)==0):
                bss = bss+1
    
        return bss



def main():
#{{{       

    sol = Solution()



    s1      = "RLRRLLRLRL"
    ans1    = 4

    sol1 = sol.balancedStringSplit(s1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)

    
    #
    s2      = "RLLLLRRRLR"
    ans2    = 3

    sol2 = sol.balancedStringSplit(s2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)

    #
    s3      = "LLLLRRRR"
    ans3    = 1

    sol3 = sol.balancedStringSplit(s3)

    print(sol3)
    print(ans3)
    assert(ans3 == sol3)

    #
    s4      = "RLRRRLLRLL"
    ans4    = 2

    sol4 = sol.balancedStringSplit(s4)

    print(sol4)
    print(ans4)
    assert(ans4 == sol4)

#}}} 


      
if __name__ == "__main__":
    main()
