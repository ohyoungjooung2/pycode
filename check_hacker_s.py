#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
def checkIfHacker(s):
    str = 'hackerrank'
    if len(s) < len(str):
       return "NO"

    j = 0
    for i in range(len(s)):
        if j < len(str) and s[i] == str[j]:
           j+=1

    if j == len(str):
       return "YES"
    else:
       return "NO"

s="hcccchhccckkkeeerrraaannkkk"
//print(checkIfHacker(s))

#Java code
#public class checkIfIsHacker {
#	public static void main (String args[]) {
#		String s = "haackkkerrrraaaannnkkke";
#		System.out.println(checkIfHackerc(s));
#	}
#	public static String checkIfHackerc(String s) {
#		String str = "hackerrank";
#		if (s.length() < str.length()) {
#			return "NO";
#		}
#		
#		int j = 0;
#		for (int i = 0; i < s.length(); i++) {
#			if (j < str.length() && s.charAt(i) == str.charAt(j)) {
#				j++;
#			}
#		}
#		
#	return (j == str.length() ? "YES" : "NO");
#    }
#
#}
