#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        depth   = 0
        stk     = []
        decomp  = []
        rmOuter = []

        for i in range(len(S)):
            decomp.append(S[i])
            if S[i]=='(':
                stk.append(S[i])
                depth += 1
            elif S[i]==')':
                if stk[-1]=='(':
                    stk.pop()
                    depth -= 1
                    if(depth==0):
                        rmOuter.extend(decomp[1:-1])
                        decomp = []
                else:
                     pass
            else:
                pass


        return "".join(rmOuter)


def main():
#{{{       

    sol = Solution()



    s1      = "(()())(())"
    ans1    = "()()()"

    sol1 = sol.removeOuterParentheses(s1)

    print(sol1)
    print(ans1)
    assert(ans1 == sol1)

#  
    s2      = "(()())(())(()(()))"
    ans2    = "()()()()(())"

    sol2 = sol.removeOuterParentheses(s2)

    print(sol2)
    print(ans2)
    assert(ans2 == sol2)

#  
    s3      = "()()"
    ans3    = ""

    sol3 = sol.removeOuterParentheses(s3)

    print(sol3)
    print(ans3)
    assert(ans3 == sol3)




#}}} 


      
if __name__ == "__main__":
    main()
