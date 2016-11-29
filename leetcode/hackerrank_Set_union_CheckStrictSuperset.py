"""
You are given one set  and a number of other sets, . 
Your job is to find whether set  is a strict superset of all the  sets. 
Print True, if  is a strict superset of all of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example: 
Set is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set.

Input Format

The first line contains the space separated elements of set .
The second line contains integer , the number of other sets.
The next  lines contains the space separated elements of the other sets.

Constraints

 

 

Output Format

Print True if set  is a strict superset of all other  sets. Otherwise, print False.

Sample Input

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output

False
Explanation

Set  is the strict superset of the set but not of the set because  is not in set .
Hence, the output is False.
"""





A = set(input().split())
result = True
for n in range(int(input())):
    B = set(input().split())
    if A-B != A^B:
        result = False
print(result)




A = set(input().split())
print(all(A > set(input().split()) for n in range(int(input()))))