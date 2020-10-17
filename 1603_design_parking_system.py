#!/usr/bin/env python3

# -*- coding: UTF-8 -*-
import sys
import os
from copy import deepcopy
import math

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        
        self.big = big
        self.medium = medium
        self.small = small


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """

        if carType==1:
            if self.big==0:
                return False
            else:
                self.big-=1
                return True
        elif carType==2:
            if self.medium==0:
                return False
            else:
                self.medium-=1
                return True
        elif carType==3:
            if self.small==0:
                return False
            else:
                self.small-=1
                return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

def main():
#{{{       

    parkingSystem = ParkingSystem(1, 1, 0);
    assert(parkingSystem.addCar(1)==True) # return true because there is 1 available slot for a big car
    assert(parkingSystem.addCar(2)==True) # return true because there is 1 available slot for a medium car
    assert(parkingSystem.addCar(3)==False) # return false because there is no available slot for a small car
    assert(parkingSystem.addCar(1)==False) # return false because there is no available slot for a big car. It is already occupied.

  

#}}} 


      
if __name__ == "__main__":
    main()
