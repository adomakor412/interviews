#!/usr/bin/env python3

import sys

def multiply(x,y):#multiply two n-digit numbers
    n = len(str(x))
    if n == 1:
        return x*y
    
    #x= 10**(n/2)*a+b
    #y= 10**(n/2)*c+d
    a = int(str(x)[0])
    b = int(str(x)[1])
    c = int(str(y)[0])
    d = int(str(y)[1])
    p = a + b
    q = c + d
    ac = a*c
    bd = b*d
    pq = p*q
    adbc = pq - ac - bd
    return 10**n*(ac)+10**(n/2)*(adbc)+b*d
    
def main(x,y):
    print (multiply(x,y))

if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    main(x,y)
