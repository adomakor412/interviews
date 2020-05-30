#!/usr/bin/env python3

import sys

def multiply(x,y):#multiply two n-digit numbers
    n = len(str(x))
    #x= 10**(n/2)*a+b
    #y= 10**(n/2)*c+d
    a = int(str(x)[0])
    b = int(str(x)[1])
    c = int(str(y)[0])
    d = int(str(y)[1])
    return 10**n*(a*c)+10**(n/2)*(a*d+b*c)+b*d
    
def main(x,y):
    print (multiply(x,y))

if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    main(x,y)

