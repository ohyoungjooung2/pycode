#!/usr/bin/env python3
#n is same with each n**len(str(n))'s sum.
#153 is armstrong num,cause (1**3)+(5**3)+(3**3)=>153, so 153 is armstrong num.
#First method
def armOrNot(n):
    r=0
    sn=str(n)
    nlen=len(sn)
    for i in sn:
        r+=(int(i)**nlen)
    if r == n:
       print(f'{n} is armstrong numbber')
    else:
       print(f'{n} is not armstrong numbber')

#for i in range(10000):
#    armOrNot(i)
armOrNot(153)

#Second method
def isArmstrong(n):
    r=0
    nr=n
    nlen=len(str(n))
    while(nr != 0):
        t=nr%10
        r=r+(t**nlen)
        nr=nr//10
    if (r == n):
        print(f'{n} is armstrong number')
    else:
        print(f'{n} is not armstrong number')

isArmstrong(153)
#Java Code(java 8 tested)
#public class ArmStrongNum {
#    static void isArmstrong(int num) {
#	 String snum = Integer.toString(num);
#	 int snumLen = snum.length();
#	 int result = 0;
#	 int num2 = num;
#	 while (num2 != 0) {
#		int t = num2 % 10;
#		result = (int) (result + (Math.pow(t,snumLen)));
#		num2 = (num2 / 10);
#	 }
#	 if (result == num) {
#		 System.out.println(num + " is Armstrong number");
#	 }
#	// else {
#	//	 System.out.println(num + " is not Armstrong number");
#	 //}
#	 //System.out.println(snum.length());
#	// return num;
#	}
#
#	public static void main(String[] args) {
#		//System.out.println(randList);
#		isArmstrong(153);
#		for (int i=1; i<=1000; i++) {
#			isArmstrong(i);
#		}
#  }
#
#
#}
