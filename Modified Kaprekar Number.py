#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    c=0
    while(p!=q+1):
        l=1
        while l<=p:
            l=l*10
        if p==(p*p)//l + (p*p)%l :
            print(p,end=" ")
            c=c+1
        p=p+1    
    if c==0:
        print("INVALID RANGE")
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
