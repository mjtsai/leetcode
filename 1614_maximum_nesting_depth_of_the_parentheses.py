#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_depth   = 0
        depth       = 0
        stk         = []

        for i in range(len(s)):
            if s[i]=='(':
                stk.append(s[i])
                depth += 1
            elif s[i]==')':
                if stk[-1]=='(':
                    if depth>max_depth:
                        max_depth = depth
                    stk.pop()
                    depth -= 1
                else:
                    pass
            else:
                pass


        return max_depth


def main():
#{{{       

    sol = Solution()



    s1      = "(1+(2*3)+((8)/4))+1"
    ans1    = 3

    sol1 = sol.maxDepth(s1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)

#

    s2      = "(1)+((2))+(((3)))"
    ans2    = 3

    sol2 = sol.maxDepth(s2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)


#

    s3      = "1+(2*3)/(2-1)"
    ans3    = 1

    sol3 = sol.maxDepth(s3)

    print(sol3)
    print(ans3)
    assert(ans3 == sol3)
  

#}}} 


      
if __name__ == "__main__":
    main()
