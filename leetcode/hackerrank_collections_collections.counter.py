"""
collections.Counter() 
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Sample Code

>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
Task

 is a shoe shop owner. His shop has  number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes. 
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers. 
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Constraints

 
 
 

Output Format

Print the amount of money earned by .

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
Explanation

Customer 1: Purchased size 6 shoe for $55. 
Customer 2: Purchased size 6 shoe for $45. 
Customer 3: Size 6 no longer available, so no purchase. 
Customer 4: Purchased size 4 shoe for $40. 
Customer 5: Purchased size 18 shoe for $60. 
Customer 6: Size 10 not available, so no purchase.

Total money earned =  
"""



from collections import Counter
X = int(input())
sizedict = Counter(input().split())
total = 0
for _ in range(int(input())):
    size,price = input().split()
    if sizedict[size]:
        total += int(price)
        sizedict[size] -= 1
print(total)




"""
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but it has one difference: The value fields' data type is specified upon initialization. 
For example:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])
In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

Constraints 
 
 

Input Format

The first line contains integers,  and  separated by a space. 
The next  lines contains the words belonging to group . 
The next  lines contains the words belonging to group .

Output Format

Output  lines. 
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions ,  and . 
'b' appeared  times in positions  and . 
In the sample problem, if 'c' also appeared in word group , you would print .
"""
from collections import defaultdict
n,m = map(int,input().split())
A = defaultdict(list)
B = []
for _ in range(n):
    A[input()].append(_+1)
for _ in range(m):
    B.append(input())
for n in B:
    if A[n]:
        print(" ".join(map(str,A[n])))
    else:
        print(-1)

		
		
		
"""
Collections.namedtuple()	

collections.namedtuple()

Basically, namedtuples are easy to create, lightweight object types. 
They turn tuples into convenient containers for simple tasks. 
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Example

Code 01

>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
Code 02

>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y
Task

Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .

Your task is to help Dr. Wesley calculate the average marks of the students.


Note: 
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet. 
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer , the total number of students. 
The second line contains the names of the columns in any order. 
The next  lines contains the , ,  and , under their respective column names.

Constraints


Output Format

Print the average marks of the list corrected to 2 decimal places.

Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
TESTCASE 02

5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00
Explanation

TESTCASE 01

Average = 

Can you solve this challenge in 4 lines of code or less? 
NOTE: There is no penalty for solutions that are correct but have more than 4 lines.
"""

N, marks = int(input()),input().split().index("MARKS")
print("%.2f" %(sum(int(input().split()[marks]) for _ in range(N))/N))


from collections import namedtuple
N,sheet = int(input()),namedtuple("sheet",input())
#print(sheet(*input().split()))
#sheet(ID='1', MARKS='97', NAME='Raymond', CLASS='7')
print("%.2f" %(sum(float(sheet(*input().split()).MARKS) for _ in range(N))/N))





"""
Collections.OrderedDict()
collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Example

Code

>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
Task

You are the manager of a supermarket. 
You have a list of  items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item. 
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, . 
The next  lines contains the item's name and price, separated by a space.

Constraints


Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
Explanation

BANANA FRIES: Quantity bought: , Price:  
Net Price:  
POTATO CHIPS: Quantity bought: , Price: 
Net Price:  
APPLE JUICE: Quantity bought: , Price:  
Net Price:  
CANDY: Quantity bought: , Price:  
Net Price: 
"""


from collections import OrderedDict
dic = OrderedDict()
for _ in range(int(input())):
    item_name,price = input().rsplit(" ",1)
    dic[item_name] = dic.get(item_name,0)+int(price)
#    if item_name in dic:
#        dic[item_name] += int(price)
#    else:
#        dic[item_name] = int(price)
for n in dic.items():
    print(*n)	


	
from collections import OrderedDict
from collections import Counter
dic = OrderedDict()
itemcounter = []
for _ in range(int(input())):
    item_name,price = input().rsplit(" ",1)
    itemcounter.append(item_name)
    dic[item_name] = int(price)
for n, p in dic.items():
    print(n,p*Counter(itemcounter)[n])
	
	
	
	
"""
Word Order
You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints: 
 
The sum of the lengths of all the words do not exceed  
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, . 
The next  lines each contain a word.

Output Format

Output  lines. 
On the first line, output the number of distinct words from the input. 
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
"""
	
from collections import Counter
lst = []
for _ in range(int(input())):
    lst.append(input().strip())
dic = Counter(lst)
print(len(dic))
for n in lst:
    k = dic.pop(n,None)
    if k == None:
        continue
    else:
        print(k, end =" ")
		
from collections import OrderedDict
dic = OrderedDict()
for _ in range(int(input())):
    word = input().strip()
    dic[word] = dic.get(word,0) + 1
print(len(dic))
print(*dic.values())	


from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())	



"""
collections.deque()

A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

Click on the link to learn more about deque() methods. 
Click on the link to learn more about various approaches to working with deques: Deque Recipes.

Example

Code

>>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
deque([2, 1])
>>> d.clear()
>>> print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9'])
Task

Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer , the number of operations. 
The next  lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
"""
from collections import deque
lst = deque()
for _ in range(int(input())):
    eval("lst.{0}({1})".format(*(input().split()+[" "])))
print(*lst)


from collections import deque
lst = deque()
for _ in range(int(input())):
    cmd,*args = input().split()
#	cmd = input().split()
    getattr(lst, cmd)(*args)
#	getattr(lst, cmd[0])(*[cmd[1]] if len(cmd) > 1 else [])
print(*lst)
"""
Piling Up!
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer , the number of test cases. 
For each test case, there are  lines. 
The first line of each test case contains , the number of cubes. 
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Constraints 
 
 

Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2
Sample Output

Yes
No
Explanation

In the first test case, pick in this order: left - , right - , left - , right - , left - , right - . 
In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .
"""
from collections import deque
for _ in range(int(input())):
    n, lst = int(input()),deque(map(int,input().split()))
    for number in sorted(lst,reverse=True):
        if number == lst[0]:
            lst.popleft()
        elif number == lst[-1]:
            lst.pop()
        else:
            print("No")
            break
    else:
        print("Yes")

"""
Most Common
You are given a string . 
The string contains only lowercase English alphabet characters.

Your task is to find the top three most common characters in the string .

Input Format

A single line of input containing the string .

Constraints


Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in ascending order.

Sample Input

aabbbccde
Sample Output

b 3
a 2
c 2
Explanation

Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c.

Note: The string  has at least  distinct characters.
"""


from collections import Counter
S = input().strip()
dic = Counter(S)
for n in sorted(dic.items(),key = lambda x: (-x[1], x[0]))[0:3]:       
    print(" ".join(str(o) for o in n),sep=' ')






