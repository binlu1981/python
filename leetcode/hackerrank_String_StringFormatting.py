"""
Read the integer,  and print the decimal, octal, hexadecimal, and binary values from  to  with space padding so that all fields take the same width as the binary value.

Input Format 
The first line contains an integer, .

Constraints

Output Format 
Print  lines. Format the fields as the width of the binary value of .

Sample Input

17
Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001     
"""
N = int(input())
width = len("{0:b}".format(N))
for n in range(1,N+1):
    print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(n,w=width))
	
	
	
	