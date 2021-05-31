#https://www.hackerrank.com/challenges/cut-the-sticks/problem
def st(n):
    from collections import Counter
    b=dict(Counter(sorted(n)))
    r=[]
    r.append(len(n))
    tlen=len(n)
    for k,v in b.items():
        if tlen-v != 0:
           r.append(tlen-v)
           tlen=tlen-v
    return r


#a=[1,2,2,3,3,4]
a=[1]
a=[1,2,2,3,3,4]
a=[5,4,4,2,2,8]

print(st(a))
#package tst;
#
#import java.util.Scanner;
#import java.util.Arrays;
#public class Solution {
#	public static void main(String[] args) {
#		/* Save Input */
#		Scanner scan = new Scanner(System.in);
#		int numSticks = scan.nextInt();
#		int [] array = new int[numSticks];
#		for (int i = 0; i < numSticks; i++) {
#			array[i] = scan.nextInt();
#		}
#		scan.close();
#		Arrays.sort(array);
#        System.out.println(array.length);
#		for (int i = 1; i < array.length; i++) {
#			//System.out.println(i);
#			//System.out.println(array[i]);
#			if (array[i] != array[i-1]) {
#				System.out.println(array.length-i);
#
#			}
#			
#		}
#				
#	}
#
#}
