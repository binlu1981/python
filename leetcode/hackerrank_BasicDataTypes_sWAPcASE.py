"""
You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string .

Constraints


Output Format

Print the modified string .

Sample Input

HackerRank.com presents "Pythonist 2".
Sample Output

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""


S = input()
lst = []
for n in S:
    if n.isupper():
        lst.append(n.lower())
    else:
        lst.append(n.upper())
print(''.join(lst))


print("".join([n.lower() if n.isupper() else n.upper() for n in input()]))


print(input().strip().swapcase())