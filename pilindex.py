#https://www.hackerrank.com/challenges/palindrome-index/copy-from/177043277
#This algo rithem is the one that requires the index, which if we remove, the whole string would be pilandrom like 'aa','aca',bcb'...
def pi(s):
   if s == s[::-1]:
      return -1

   lis=list(s)
   r1=0
   r2=0
   
   for i in range(len(lis)):
       if lis[i] != lis[-(i+1)]:
           #print(i,-(i+1))
           r1=i
           r2=-(i+1)
           r2=len(lis)+r2
           break;

   del lis[r1]
   if lis == lis[::-1]:
      return r1
   else:
      return r2


#e='hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'
#print(pi(a))
#print(pi(b))
#print(pi(c))
#print(pi(d))
#print(pi(e))


#Slow solution(it gets time limie)
#def palindromeIndex(s):
#    if s == s[::-1]:
#        return -1
#
#    lis=list(s)
#    lisb=list(lis)
#    for i in range(len(lis)):
#        del lisb[i]
#        if lisb == lisb[::-1]:
#            return i
#        else:
#           lisb=list(lis)
#
#Given a string of lowercase letters in the range ascii[a-z], determine a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. For example, if your string is "bcbc", you can either remove 'b' at index or 'c' at index
#
#. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.
#
#Function Description
#
#Complete the palindromeIndex function in the editor below. It must return the index of the character to remove or
#
#.
#
#palindromeIndex has the following parameter(s):
#
#    s: a string to analyze
#
#Input Format
#
#The first line contains an integer
#, the number of queries.
#Each of the next lines contains a query string
#
#.
#
#Constraints
#
#    All characters are in the range ascii[a-z].
#
#Output Format
#
#Print an integer denoting the zero-indexed position of the character to remove to make
#a palindrome. If is already a palindrome or no such character exists, print
#
#.
#
#Sample Input
#
#3
#aaab
#baa
#aaa
#
#Sample Output
#
#3
#0
#-1
#
#Explanation
#
#Query 1: "aaab"
#Removing 'b' at index
#results in a palindrome, so we print
#
#on a new line.
#
#Query 2: "baa"
#Removing 'b' at index
#results in a palindrome, so we print
#
#on a new line.
#
#Query 3: "aaa"
#This string is already a palindrome, so we print
#
#. Removing any one of the characters would result in a palindrome, but this test comes first.
#
#Note: The custom checker logic for this challenge is available here.
