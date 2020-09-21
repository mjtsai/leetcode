#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        address = address.replace('.', '[.]')
        return address




def main():
#{{{       

    sol = Solution()




    address0    = "1.1.1.1"
    ans0        = "1[.]1[.]1[.]1"

    sol0 = sol.defangIPaddr(address0)

    print(ans0)
    assert(ans0 == sol0)


    #
    address1    = "255.100.50.0"
    ans1        = "255[.]100[.]50[.]0"

    sol1 = sol.defangIPaddr(address1)

    print(ans1)
    assert(ans1 == sol1)

#}}} 


      
if __name__ == "__main__":
    main()
