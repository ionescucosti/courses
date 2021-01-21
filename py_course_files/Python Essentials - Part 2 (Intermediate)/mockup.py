'''
str='abcdef'
def fun(s):
    del s[2]
    return s
print(fun(str))
###############################
print('a','b','c',sep="'")
###############################
class A:
    A=1
    def __init__(self):
        self.a=0
print(hasattr(A,'A'))
###############################
i=4
while i>0:
    i-=2
    print('*')
    if i==2:
        break
else:
    print('*')
###############################
class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g():
        return self.f()
a=A()
print(a.g())
There is one fundamental requirement - a method is obliged to have at least one parameter (there are no such thing as parameterless methods - a method may be invoked without an argument, but not declared without parameters).
###############################
str1='string'
str2=str1[:]
###############################
print(len((1,)))
###############################
class Class:
    def __init__(self):
        pass
object = Class()
###############################
def a(x):
    def b():
        return x+x
    return b
x=a('X')
y=a('')
print(x()+y())
###############################
v = 1 + 1 // 2 + 1 / 2 + 2
print(v)
###############################
t=(1,2,3,4)
t=t[-2:-1]
t=t[-1]
print(t)
###############################
d={'one':1, 'three':3, 'two':2}
for k in sorted(d.values()):
    print(k,end=' ')
###############################
class A:
    def a(self):
        print('a')
class B:
    def a(self):
        print('b')
class C(A,B):
    def c(self):
        self.a()
o=C()
o.c()
###############################
class A:
    A=1
    def __init__(self,v=2):
        self.v = v +A.A
        A.A += 1
    def set(self,v):
        self.v += v
        A.A +=1
        return
a = A()
a.set(2)
print(a.v)
###############################
a=True
b=False
a=a or b
b=a and b
a=a or b
print(a,b)
###############################
x=16
while x>0:
    print('*',end='')
    x//=2
###############################
ls = [[c for c in range(r)] for r in range(3)]
c=0
for x in ls:
    if len(x)<2:
        c+=1
print(c)
###############################
try:
    raise Exception
except BaseException:
    print('a',end='')
else:
    print('b',end='')
finally:
    print('c')
###############################
class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass

x=X()
z=Z()
print(isinstance(x,Z), isinstance(z,X))
###############################
x='\'
print(len(x))
###############################
s=open('f.txt','r')
q=s.readlines()
print(type(q))
###############################
d= {1:0, 2:1, 3:2, 0:1}
x= 0

for y in range(len(d)):
    x = d[x]
    print(x)

print(x)
###############################
def fun(d,k,v):
    d[k]=v
dc={}
print(fun(dc,'1','v'))
print(dc)
###############################
def fun(x):
    return 1 if x%2 != 0 else 2
print(fun(fun(1)))
###############################
class A:
    pass
class B:
    pass
class C(A,B):
    pass
print(issubclass(C,A) and issubclass(C,B))
###############################
x,y,z=3,2,1
z,y,x=x,y,z
print(x,y,z)
###############################
y=input()
x=input()
print(x+y)
###############################
class A:
    def __init__(self,v):
        self.__a = v + 1
a=A(0)
print(a.__a)
###############################
t=(1, )
t=t[0]+t[0]
print(t)
###############################
lt=[1,2,3,4]
lt=list(map(lambda x: 2*x, 1))
print(lt)
###############################
class A:
    def __init__(self,name):
        self.name=name
a=A('class')
print(a)
###############################
def fun(a,b,c=0):
    pass
fun(a=1,b=0,c=0)
###############################
d={}
d['2']={1,2}
d['1']={3,4}
for x in d.keys():
    print(d[x][1],end='')
###############################
try:
    raise Exception
except:
    print("c")
except BaseException:
    print('a')
except Exception:
    print("b")
###############################
print(len([i for i in range(0,-2)]))
###############################
def I(n):
    s=''
    for i in range(n):
        s += '+'
        yield s

for x in I(3):
    print(x,end='')
###############################
def f(par2,par1):
    return par2 + par1
print(f(par2=1,2))
###############################
z=2
y=1
x= y<z or z>y and y<z or z<y
print(x)
###############################
x="Peter's sister's name's \"Anna\""
print(x)
###############################
i=250
while len(str(i))>72:
    i *=2
else:
    i//=2
print(i)
###############################
n=0
while n<4:
    n+=1
    print(n,end=' ')
###############################
Val = 1
Val2 = 0
Val = Val ^ Val2
Val2 = Val ^ Val2
Val = Val ^ Val2
print(Val)
###############################
z, y, x = 2, 1, 0
print(x, y, z)
x, z = z, y
print(x, y, z)
y = y - z
print(x, y, z)
x, y, z = y,z,x
print(x, y, z)
###############################
i = 10
while i > 0 :
 i -= 3
 print("*")
 if i <= 3:
    break
else:
 print("*")
###############################
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
###############################
s = "Hello, Python!"
print(s[-14])
print(s[13])
'''


