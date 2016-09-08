#a= int(input('hello world, please input'))
a=9
while True:
    a+=3
    if a >9:
        print(a)
        break
    else:
        print('try more bigger number')
print('hello world')

"""sum"""
l=[9,7,5,6]
tot=0
while l:
    tot+=l[0]
    l=l[1:]
    print(tot)
print(tot)
for n in l:
    tot+=n
    print(tot)

"""sumtree"""
l2=[9,8,7,[9,8,7,[9,8,7]]]
def tottree(l):
    tot=0
    for n in l:
        if not isinstance(n, list):
            tot+=n
        else:
            tot+=tottree(n)
    return tot
if __name__=="__main__":
    print(tottree(l2))

l3=[9,7,5,6]
def minone(li):
    small = li[0]
    for n in li[1:]:
        if n < small:
           small=n
    return small
print(minone(l3))

small = l3[0]
for n in l3[1:]:
    if n < small:
        small = n
print(small)

l1=[3,6,5,6]
def minone1(first,*rest):
    for n in rest:
        if n < first:
            first=n
    return first
print(minone1(l3,l1))

def minone6(arg):
    small=sorted(list(arg))[0]
    return small
print(minone6(l3))
print(minone6(l1))

"""detect prime"""
a=13
for n in range(2,a):
    if a%n==0:
        break
else:
    print("a is a prime")


import math
"""ax2+bx+c=0"""
#a = float(input("input a value "))
#b = float(input("input b value "))
#c = float(input("input c value "))
a=3
b=7
c=1
if a==0:
    x=-c/b
    print("linear, x =", x)
else:
    delt=b**2 - 4*a*c
    if delt < 0:
        print ("no real root")
    elif delt ==0:
        print ("only one root", -b/(2*a))
    else:
        root=math.sqrt(delt)
        x1=(-b+root)/(2*a)
        x2=(-b-root)/(2*a)
        print ("two solution are", x1, x2)


"""section 3.1 basketball"""

#lead_point=int(input("input the lead point: "))
lead_point=3
point=lead_point- 3
#control=raw_input("if the lead team control ball?")
control="yes"
if control=="yes":
    point+=0.5
else:
    point-=0.5
#left_time=int(input("the time left? in second"))
left_time=5
if point**2 > left_time:
    print ("it's safe for lead team")
else:
    print ("it's dangerous for lead team")






"""count"""
count=0
while count <5:
    print ("GOOD")
    count+=1

total=0
i=1
while i <11:
    total+=i
    i+=1
#    print total

print (total)



"""eggs in a basket"""
for a in range(10000):
    if a%1==0 and a%2==1 and a%3==0 and a%4==1 and a%5==1 and a%6==3 and a%7==0 and a%8==1 and a%9==0:
        print (a)


count=0

while count <5:
    if count >=3:
        break
    print("good")
    count+=1

count=0

while count <5:
    count += 1
    if count >=2:
        continue
    print("good")



"""factorial"""
import math
e=0
for i in range(100):
    e+=1.0/math.factorial(i)
print (e)
"""or"""
#e=0
factorial=1.0
#for i in range(100):
#    factorial *= i
#    e+=1.0/factorial
#    print e
#print e



"""Collatz conjecture"""

n=13
while n!=1:
    if n%2!=0:
        n=n*3+1
    else:
        n/=2
    print (n)



"""9*9"""
#for i in range(9):
#    for j in range(9):
#        print format(i*j,"3"),
#   print


"""chick"""
for chick in range(39):
    for rabbit in range (39):
        if chick + rabbit ==39 and chick *2 + rabbit *4 ==94:
            print (chick, rabbit)


"""03-3 guess"""
#x=float(input("input a number greater than 1 and 0:"))
x=9
low=0
high=x
guess=(low+high)/2
#while guess**2!=x: (this will let unlimited loop)
while abs(guess**2-x) > 0.001:
    if guess**2 < x:
        low=guess
        guess = (low + high) / 2
        print(guess)
    else:
        high=guess
        guess = (low + high) / 2
        print(guess)
print("x root is:", guess)


"""prime number"""
x=56
count_prime=0
count_noprime=0
for num in range(2,x):
    if x%num == 0:
        count_noprime+=1
        print ("this is not a prime,totally: ",count_noprime)
        break
else:
    count_prime+=1
    print("not a prime,totally: ",count_noprime)

import math
count=0
num=2
while count < 50:
    for i in range(2, int(math.sqrt(num)+1)):
        if num%i== 0:
            break
    else:
        print (num)
        count+=1
    num+=1

x=1
def f1():
    x=2
    print (x)
f1()
print (x)

def increase():
    global x
    x+=1
    print(x)
increase()
print(x)


"""jiecheng"""
n=3
x=1
i=1
while i <= n:
    x*=i
    i+=1
print (x)

def p(n):
    if n==0 or n==1:
        return n
    else:
        return n*p(n-1)
print (p(3))


def hanoi(n,A,B,C):
    if n==1:
        print ("move disk ", n,"from ",A,"to ",C)
    else:
        hanoi(n-1,A,C,B)
        print ("move disk ", n,"from ",A,"to ",C)
        hanoi(n-1,B,A,C)
n=2
hanoi(n,'left','middle','right')

"""time """
def fib_loop(n):
    if n==1 or n==2:
        return 1
    else:
        i=2
        f1=1
        f2=1
        while i<n:
            f3=f1+f2
            f1=f2
            f2=f3
            i+=1
        return f3
print (fib_loop(8))

def fib_recursive(n):
    if n==1 or n==2:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)
print(fib_recursive(8))

def yuanyin_count(stri):
    count=0
    for char in stri:
        if char in "aeiouAEIOU":
            count+=1
    return count
print yuanyin_count("agelong")


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
#soup = BeautifulSoup(open('index.html'))
print soup.prettify()
print soup.title
print soup.head
print soup.a
print soup.p
print soup.name
print soup.head.name
print soup.p.attrs
print soup.p["class"]
print soup.p.string
print soup.a
print soup.a.string
print soup.head.contents
print soup.head.contents[0]
print soup.head.children
for child in soup.body.children:
    print child
for child in soup.descendants:
    print child
print soup.head.string
print soup.title.string
for string in soup.stripped_strings:
    print(repr(string))
for parent in soup.head.title.string.parents:
    print parent.name
print soup.p.next_sibling
print soup.p.prev_sibling
print soup.p.next_sibling.next_sibling
for sibling in soup.a.next_siblings:
    print(repr(sibling))
print soup.head.next_element
#for element in last_a_tag.next_elements:
#    print(repr(element))
soup.find_all('b')
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
print soup.find_all(["a","p","b"])
for tag in soup.find_all(True):
    print(tag.name)
def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")
print soup.find_all(has_class_but_no_id)
print soup.find_all(id="link2")
print soup.find_all(href=re.compile("elsie"))
print soup.find_all(href=re.compile("elsie"),id="link1")
print soup.find_all("a",class_="sister")
print soup.find_all(text="Elsie")
print soup.find_all(text=["Tillie","Elsie","Lacie"])
print soup.find_all(text=re.compile("Dormous"))
print soup.find_all("a",limit=2)
print soup.html.find_all("title", recursive=False)
print soup.select("title")
print soup.select("a")
print soup.select(".sister")
print soup.select("#link1")
print soup.select('p #link1')
print soup.select("head > title")
print soup.select('a[class="sister"]')
print soup.select('a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
print soup.select('p a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]


"""section5 string"""

def huiwen(name):
    low=0
    upper=len(name)-1
    while low < upper:
        if name[low]!=name[upper]:
            return False
        low +=1
        upper-=1
    return True
print huiwen("B")

def huiwen1(name):
    if len(name) <1:
        return True
    if name[0]== name[-1]:
        return huiwen1(name[1:-1])
    else:
        return False
print huiwen1("BOBBOB")


def shengxu(name):
    l = len(name)
    print range(l-1)
    for i in range(l-1):
        if name[i] > name[i+1]:
            return False
    return True
print shengxu("acbd")

def shengxu1(name):
    first=name[0]
    for s in name:
        if first > s:
            return False
        else:
            first = s
    return True
print shengxu1("acb")

import re
pattern="(C.A)"
name="(Ca.A)"
result=re.search(pattern,name)
if result:
    print ("find in {}".format(name))


def bi_search(lst, number):
    lower=0
    upper=len(lst)-1
    while lower < upper:
        mid=(lower+upper)/2
        if lst[mid]<number:
            lower=mid
        elif lst[mid]==number:
            return number
        else:
            upper=midder
    return -1
print bi_search([1,3,6,7,10,12,15,18],12)


"Poker sort"
def sortlist(lst):
    for i in range(len(lst)-1):
        minindex=i
        for j in range(i+1,len(lst)):
            if lst[minindex]>lst[j]:
                minindex=j
        lst.insert(i,lst.pop(minindex))
    return lst

print sortlist([24,1,2,6,3,2,19,10])


def swap(lst,a,b):
    tmp=lst[a]
    lst[a]=lst[b]
    lst[b]=tmp

def sortlist1(lst):
    for i in range(len(lst)-1):
        minindex=i
        for j in range(i+1,len(lst)):
           if lst[minindex]>lst[j]:
               minindex=j
        swap(lst,i,minindex)
    return lst
print sortlist1([24,1,2,6,3,2,19,10])












