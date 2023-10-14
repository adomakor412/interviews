#https://stackoverflow.com/questions/28526166/odd-one-out-algorithm
#https://www.slideshare.net/allwayscollection/2-odd-one-outanalyze-the-difference-in-adjacent-letters-of-the-alpdf
'''
Odd One Out
Analyze the difference in adjacent letters of the alphabet given a string. Given an input sequence
of words, find the 'Odd One Out' by checking the difference between adjacent letters. The
element having a distinct difference is the 'Odd One Out.'
Example
series =["ACB","BDC", "CED", "DEF."]
In the first three strings, the differences between the letters are (+2, - 1) e.g. 'C' -'A' = 2 , 'B' -
'C' = - 1 . In the last string, the differences are (+1, -1) "DEF" is the odd one out.
Function Description
Complete the function findOdd in the editor.
findOdd has the following parameter(s): string series[n]: an array of strings
Returns
string: the odd one out.
Constraints
3 <= n <= 26
2 <= length of series[i] < 26
All strings are uppercase English letters only.
Within a test case, all strings are of equal length.
Input Format For Custom Testing
The first line contains an integer, n, denoting the number of elements in series. Subsequent n
lines of the ith element of series (where 0 <= i < n ).
Sample Case 0
Sample Input For Custom Testing
FUNCTION
series[] size n = 4
series =[ "ABC","BCD", "EFG", "DCB"]
Sample Output: DCB
Explanation
In the series, ABC, BCD, EFG, differences are (+1, +1). For DCB, differences are (-1, -1).
'''
def findOdd(series):
    # Calculate the difference between adjacent letters for the first word
    first_word = series[0]
    differences = [ord(first_word[i + 1]) - ord(first_word[i]) for i in range(len(first_word) - 1)]

    # Check the differences in the rest of the words and find the odd one out
    firstCase = True
    for word in series[1:]:
        current_differences = [ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1)]
        if current_differences != differences:
            if not firstCase:  
                return word
            else:
                return findOdd(series[1:] + series[0])
        firstCase = False

# Sample input
series = ["ABC", "BCD", "EFG", "DCB"]
result = findOdd(series)
print(result)
