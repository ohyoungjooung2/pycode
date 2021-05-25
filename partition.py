#https://www.hackerrank.com/challenges/quicksort1/problem
a=[4,5,3,7,2]
def pt(a):
    l=[]
    r=[]
    f=a[0]
    for i in range(1,len(a)):
        if a[i] > f:
            r.append(a[i])
        else:
            l.append(a[i])
    l.append(f)
    print(l)
    print(r)
    print(l+r)


pt(a)

#Java 8?
#import java.io.*;
#import java.util.*;
#public class Soultion {
#
#	public static void main(String[] args) {
#		int[] array = new int[5];
#	    array[0] = 5;
#	    array[1] = 3;
#	    array[2] = 2;
#	    array[3] = 7;
#	    array[4] = 8;
#	    System.out.println(quickSort(array));
#
#	}
#
#	static List<Integer> quickSort(int[] arr) {
#		List <Integer> left = new ArrayList<Integer>();
#		List <Integer> equal = new ArrayList<Integer>();
#		List <Integer> right = new ArrayList<Integer>();
#
#		int pivot = arr[0];
#		for(int i = 0; i < arr.length; i++) {
#			if (arr[i] < pivot)
#			{
#			    left.add(arr[i]);
#			}
#			else if (arr[i] == pivot)
#			{
#				equal.add(arr[i]);
#			}
#			else if (arr[i] > pivot)
#			{
#				right.add(arr[i]);
#			}
#		}
#
#		List<Integer> newList = new ArrayList<Integer>();
#		newList.addAll(left);
#		newList.addAll(equal);
#		newList.addAll(right);
#
#		System.out.println(newList);
#
#		return newList;
#
#	}
#
#}
