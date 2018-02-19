#!/usr/bin/env python3

import sys

# Code for test case 12

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    
    list = [0] * n
    highest = 0
    
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        
        for i in range(a-1, b):
          list[i] += k
          if list[i] > highest:
            highest = list[i]
            
    print(highest)
