"""
In this task , you would be given a string  of length  . You have to divide this string into  equal parts thus each part contains exactly  elements.

Let us consider the string thus obtained in part  as  . For each string  thus obtained you have to make a modified string such that each character that occurs in  occurs exactly once in the modified string.

Suppose the first occurence of  was before the first occurence of  in  . Then  should occur before in the modified string of  too. Output  lines each containing the modified string for the corresponding chunk .

Input Format

First line consists of the string .

Second line consists of  denoting the length of each of the  parts.

Output Format

 lines denoting the modified string corresponding to each chunk of string.

Constraints



It is guaranteed that  is divisible by  .

Here  denotes the length of the string .

Sample Input

AABCAAADA
3   
Sample Output

AB
CA
AD
Explanation

The string  is broken into equal parts of length  each making .

Each of these strings are modified according to the algorithm mentioned in the statement

making  and then each of these modified strings is printed in seperate lines.
"""

S,K = input(),int(input())
for n in range(0,len(S),K):
    print(''.join(sorted(set(S[0:K]),key=S.index)))
    S = S[K:]