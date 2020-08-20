#This algo problem explained form line 43(https://www.hackerrank.com/challenges/the-love-letter-mystery/problem)
s='abcd'
s='cba'
#s='abccaa'
#s='adslkfjas'
def paln(s):
    import string
    asc=string.ascii_lowercase
    ascd={}
    for i in range(len(asc)):
        ascd[asc[i]] = i
    #{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    if s == s[::-1]:
        return 0
    d=[]
    for i in s:
        d.append(ascd[i])
    
    if len(s) % 2 != 0:
       mid=int(len(d)/2)
       del d[mid]
    

    
    a=[]
    b=[]
    c=0
    print(d)
    haf=int(len(d)/2)
    for i in range(0,haf):
        a.append(d[i])
    for j in range(haf,len(d)):
        b.append(d[j])
    b=b[::-1]
    for k in range(0,haf):
        c+=abs(a[k]-b[k])
    print(a)
    print(b)
    return c

print(paln(s))
    
'''    James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

    He can only reduce the value of a letter by

    , i.e. he can change d to c, but he cannot change c to d or d to b.
    The letter a may not be reduced any further.

Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

For example, given the string

, the following two operations are performed: cde → cdd → cdc.

Function Description

Complete the theLoveLetterMystery function in the editor below. It should return the integer representing the minimum number of operations needed to make the string a palindrome.

theLoveLetterMystery has the following parameter(s):

    s: a string

Input Format

The first line contains an integer
, the number of queries.
The next lines will each contain a string

.

Constraints


| s |


All strings are composed of lower case English letters, *ascii[a-z], with no spaces.

Output Format

A single line containing the minimum number of operations corresponding to each test case.

Sample Input

4
abc
abcba
abcd
cba

Sample Output

2
0
4
2

Explanation

    For the first test case, abc → abb → aba.
    For the second test case, abcba is already a palindromic string.
    For the third test case, abcd → abcc → abcb → abca → abba.
    For the fourth test case, cba → bba → aba.
'''
