'''
print(2 ** 3 ** 2 ** 1)
print(2 ** 9)
#########################
print('Peter\'s sister\'s name\'s "Anna"')
#########################
i=250
while len(str(i)) > 72:
    i*=2
else:
    i//=2
print(i)
#########################
n=0
while n<4:
    n+=1
    print(n,end=' ')
#########################

x=0
y=2
z=len('Python')
x=y>z
print(type(x))
#########################
Val=1
Val2=0
Val=Val^Val2
print(Val)
Val2=Val^Val2
Val=Val^Val2
print(Val)
#########################
z,y,x=2,1,0
x,z=z,y
y=y-z
x,y,z=y,z,x
print(x,y,z)
#########################
a=0
b=a**0
if b<a+1:
    c=1
elif b==1:
    c=2
else:
    c=3
print(a+b+c)
#########################
i=10
while i>0:
    i-=3
    print('*')
    if i <=3:
        break
else:
    print('*')
#########################
# Example 1
for i in range(1, 4, 2):
    print("*")
# Example 2
for i in range(1, 4, 2):
    print("*", end="")
# Example 3
for i in range(1, 4, 2):
    print("*", end="**")
# Example 4
for i in range(1, 4, 2):
    print("*", end="**")
print("***")
#########################
x='20'
y='30'
print(x>y)
#########################
s = "Hello, Python!"
print(s[-14:100])
#########################
lst = ["A", "B", "C", 2, 4]
del lst[0:-2]
print(lst)
#########################
dict = { 'a': 1, 'b': 2, 'c': 3 }
for i in dict:
    print(i)
#########################
s = 'python'
for i in range(len(s)):
    i = s[i].upper()
print(s, end="")
#########################
lst = [i // i for i in range(0,4)]
sum = 0
for n in lst:
    sum += n
print(sum)
#########################
lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*', end='')
print(lst)
#########################
lst = [2 ** x for x in range(0, 11)]
print(lst[-1])
#########################
lst1 = "12,34"
lst2 = lst1.split(',')
print(len(lst1) < len(lst2))
#########################
def fun(a, b=0, c=5, d=1):
    return a ** b ** c
print(fun(b=2, a=2, c=3))
#########################
x = 50
f = lambda x: 1 + 2
print(f(x))
#########################
from math import pi as xyz # line 01
print(pi) # line 02
#########################
What is true about the __init__.py file? (Select all that apply)
B. It can execute an initialization code for a package
C. It is required to make Python treat a given directory as a Python package directory
#########################
from random import randint
for i in range(10):
    print(random(1, 5))
#########################
x = 1 # line 1
def a(x): # line 2
    return 2 * x # line 3
x = 2 + a(x) # line 4
print(a(x)) # line 5
#########################
a = 'hello'
def x(a,b):
    z = a[0]
    return z
print(x(a))
#########################
s = 'SPAM'
def f(x):
    return s + 'MAPS'
print(f(s))
#########################
Select the true statements: (select all that apply)
B. The order of arguments matters when they are passed positionally
D. A function can be called with a mix of positional and keyword arguments
#########################
def gen():
    lst = range(5)
    for i in lst:
        yield i*i
for i in gen():
    print(i, end="")
#########################
Select the true statements: (select all that apply)
A. The class keyword marks the beginning of the class definition
C. A class may define an object
D. A constructor is used to instantiate an object
#########################
Select the true statements: (select all that apply)
A. Inheritance means passing attributes and methods from a superclass to a subclass
C. Multiple inheritance means that a class has more than one superclass
D. Polymorphism is the situation in which a subclass is able to modify its superclass behavior
#########################
Select the true statements: (select all that apply)
C. A class constructor cannot return a value
D. __bases__ is a tuple filled with the names of all the direct superclasses
#########################
# Example 1
x = 1
y = 0
z = x%y
print(z)
# Example 2
x = 1
y = 0
z = x/y
print(z)
#########################
x = 0
try:
    print(x)
    print(1 / x)
except ZeroDivisionError:
    print("ERROR MESSAGE")
finally:
    print(x + 1)
print(x + 2)
#########################
class A:
    def a(self):
        print("A", end='')

class B(A):
    def a(self):
        print("B", end='')

class C(B):
    def b(self):
        print("B", end='')

a = A()
b = B()
c = C()
a.a()
b.a()
c.b()
#########################
try:
    print("Hello (non-empty line)")
    raise Exception('(empty line)')
    print(1/0)
except Exception as e:
    print(e)
#########################
# Example 1
class CriticalError(Exception):
    def __init__(self, message='ERROR MESSAGE A'):
        Exception.__init__(self, message)
raise CriticalError
raise CriticalError("ERROR MESSAGE B")

# Example 2
class CriticalError(Exception):
    def __init__(self, message='ERROR MESSAGE A'):
        Exception.__init__(self, message)
raise CriticalError("ERROR MESSAGE B")
#########################
file = open('f.txt')
print(file.readlines())
for l in file:
    print(l)
print(file.read())
file.close()
#########################
The following code snippet when run
f = open("file.txt", "w") f.close()
will (select all that apply):
A. open the file file.txt in write mode
B. delete the file contents if the file file.txt already exists
D. create the file file.txt if it does not exist
#########################
i=5
while i>0:
    while i%2!=0:
        i-=1
    else:
        i-=1
print(i)
'''