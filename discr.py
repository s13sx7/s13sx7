import math
from colorama import init
init()
from colorama import Fore, Back, Style
a = input("a=" )
b = input("b=" )
c = input("c=" )
try:
    a = int(a)
    b = int(b)
    c = int(c)
except:
    print("only numbers")
    exit(1)
if a == 0:
    print(Fore.RED, "variable cannot be zero")
    exit(1)
D= b**2-4*a*c
print(Fore.YELLOW,"discriminant",D)
if D>0:
    x1= (-b - (math.sqrt(D))) / (2 * a)
    x2= (-b + (math.sqrt(D))) / (2 * a)
    print(Fore.LIGHTBLUE_EX, 'x1 = %.2f, x2 = %.2f' % (x1,x2) )
if D==0:
    x= -b / (2 * a)
    print(Fore.Magenta, "Equation 1 has a root:",x )
