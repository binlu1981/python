"""
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output

Berry
Harry
Explanation

There are  students in this class whose names and grades are assembled to build the following list:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""

#way one
N = int(input())
nestlst = [[input(),float(input())] for _ in range(N)]
secondlowest = sorted(list(set(s for n, s in nestlst)))[1]
print('\n'.join([lst[0] for lst in sorted(nestlst) if lst[1] == secondlowest]))

#way two
N = int(input())
dic = dict((input(),float(input())) for _ in range(N))
dic1 = {}
for k, v in dic.items():
    if v in dic1:
        dic1[v].append(k)  # [k] must be a list
    else:
        dic1[v]=[k]
for name in dic1[sorted(dic1)[1]]:
    print(name)



