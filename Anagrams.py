#!/usr/bin/python3

from collections import Counter

def getAnagram(s):
    #n = -1
    length = len(s)
    if length%2 != 0:
        #pass
        return -1
    else:
        first_half, second_half = s[:length//2], s[length//2:]

        #Count frequencies
        count1 = Counter(first_half)
        count2 = Counter(second_half)

        #Calculate replacements
        n = 0
        for digit in count1:
            if count1[digit] > count2[digit]:
                n+= count1[digit] - count2[digit]
        return n