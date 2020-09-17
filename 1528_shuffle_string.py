#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy


class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
        assert(len(s)==len(indices))
        assert(len(s)>=1 and len(s)<=100)
        for c in s:
            assert(c>='a' and c<='z')
        for i in indices:
            assert(i>=0 and i<len(s))


        sf = len(s)*[None]
        for i in range(len(s)):
            sf[indices[i]] = s[i]

        return "".join(sf)


def main():
#{{{       

    sol = Solution()


    s0      = "codeleet"
    indices0= [4,5,6,7,0,2,1,3]
    ans0    = "leetcode"

    sol0 = sol.restoreString(s0, indices0)

    print(ans0)
    assert(ans0 == sol0)

    #        


    s1      = "abc"
    indices1= [0,1,2]
    ans1    = "abc"

    sol1 = sol.restoreString(s1, indices1)

    print(ans1)
    assert(ans1 == sol1)


    #
    s2      = "aiohn"
    indices2= [3,1,4,2,0]
    ans2    = "nihao"

    sol2 = sol.restoreString(s2, indices2)

    print(ans2)
    assert(ans2 == sol2)


    #
    s3      = "aaiougrt"
    indices3= [4,0,2,6,7,3,1,5]
    ans3    = "arigatou"

    sol3 = sol.restoreString(s3, indices3)

    print(ans3)
    assert(ans3 == sol3)

    #
    s4      = "art"
    indices4= [1,0,2]
    ans4    = "rat"

    sol4 = sol.restoreString(s4, indices4)

    print(ans4)
    assert(ans4 == sol4)


#}}} 


      
if __name__ == "__main__":
    main()
