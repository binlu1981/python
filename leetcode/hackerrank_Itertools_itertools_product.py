"""
itertools.product()

This tool computes the cartesian product of input iterables. 
It is equivalent to nested for-loops. 
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

Sample Code

>>> from itertools import product
>>>
>>> print list(product([1,2,3],repeat = 2))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
>>>
>>> print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
>>>
>>> A = [[1,2,3],[3,4,5]]
>>> print list(product(*A))
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
>>>
>>> B = [[1,2,3],[3,4,5],[7,8]]
>>> print list(product(*B))
[(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
Task

You are given a two lists  and . Your task is to compute their cartesian product X.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format

The first line contains the space separated elements of list . 
The second line contains the space separated elements of list .

Both lists have no duplicate integer elements.

Constraints

 

Output Format

Output the space separated tuples of the cartesian product.

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
""" 
 
 
 
 
 
from itertools import product
A,B = [list(map(int,input().split())) for _ in range(2)]
print(*product(A,B))





"""
Maximize It!
You are given a function .

You are also given  lists. The  list consists of  elements.

You have to pick exactly one element from each list so that the equation below is maximized: 

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Input Format 
The first line contains  space separated integers  and . 
The next  lines each contains an integer  followed by  space separated integers denoting the elements in the list.

Output Format 
Output a single integer denoting the value .

Constraints 
 
 
 

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
Explanation

Picking  from the st list,  from the nd list and  from the rd list gives the maximum  value equal to % = .
"""
K,M = list(map(int,input().split()))
arrayK = []
arrayK.extend([list(map(int,input().split()[1:])) for _ in range(K)])
from itertools import product
combinations = list(product(*arrayK))
#S = [sum(n*n for n in lst)%M for lst in combinations]
#print(max(S))
def fuc_modulo(lst):
    return sum(n*n for n in lst)%M
print(max(list(map(fuc_modulo,combinations))))
