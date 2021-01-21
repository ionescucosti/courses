'''
##########################
class A:
    def a(self):
        print('a')
class B:
    def a(self):
        print('b')
class C(B,A):
    def c(self):
        self.a()
o=C()
o.c()
##########################
try:
    raise Exception
except:
    print('c')
except BaseException:
    print('a')
except Exception:
    print('b')
##########################
try:
    raise Exception
except BaseException:
    print('a')
except Exception:
    print('b')
except:
    print('c')
##########################
print(len('\\\'))
print(len('\\\\'))
##########################
print(chr(ord('p')+2))
##########################
for x in open('file.txt','r'):
    print(x,len(x))
##########################
from Exercises.sudoku import checksubsquare
##########################
import math
print(dir(math))
##########################
class Class:
    def __init__(self,val=0):
        pass
object4 = Class(1,2)
##########################
print(float('1.3'))
##########################
class A:
    A=1
    def __init__(self):
        self.a=0
print(hasattr(A,'a'))
##########################
print(__name__)
##########################
from Exercises.sudoku import check
check(lst)
##########################
class A:
    def __init__(self,v=2):
        self.v=v
    def set(self,v=1):
        self.v += v
        return self.v
a=A()
b=a
b.set()
print(a.v)
##########################
def dun(d,k,v):
    d[k]=v
dc={}
print(fun(dc,'1','v'))
##########################
v=1+1//2+1/2+2
print(v)
##########################
x="""
"""
print(len(x))
##########################
try:
    raise Exception
except BaseException:
    print('a')
else:
    print('b')
finally:
    print('c')
##########################
x=16
while x>0:
    print('*',end='')
    x//2
##########################
try:
    raise Exception
except:
    print('ValidatorCNP')
finally:
    print('gata')
##########################
def I(n):
    s='+'
    for i in range(n):
        s+=s
        yield s

for x in I(2):
    print(x,end='')
##########################
from Exercises import sudoku
sudoku.check()
##########################
'''

