import sympy as sym
import os #For clearing the terminal (or console) screen everytime by calling os.system('cls')
from sympy import *

a = sym.Rational(1, 2)
os.system('cls')    #This is equivalent to clrscr() in c or clc in MATLAB.

"""
# Using sympy as a calculator
print(a)
print(a*2)
print(sym.pi)
print(sym.pi**2)
print(sym.pi.evalf())
print(sym.exp(1).evalf())
print((sym.pi + sym.exp(1)).evalf())

b = (sym.oo > 99999999) #sym.oo is infinity
print(b)
print(sym.oo+1)     #infinity+1 is also infinity
"""

""" Exercises

Calculate \sqrt{2} with 100 decimals.
Calculate 1/2 + 1/3 in rational arithmetic.

print(N(sqrt(2),100))   #obtaining 100 decimal places of any irrational number (https://docs.sympy.org/latest/modules/evalf.html)

num1 = sym.Rational(1,2)
num2 = sym.Rational(1,3)
print(num1+num2)
"""
"""
=============================================================
"""

# Symbols - Algebraic manipulations

sym.init_printing(use_unicode=False, wrap_line=True)
x = sym.Symbol('x')
y = sym.Symbol('y')
#z = x+y+x-y
#z = sym.expand((x+y)**2)
#z = sym.expand(x + y, complex=True)
# print(sym.I * sym.im(x) + sym.I * sym.im(y) + sym.re(x) + sym.re(y))
# print(sym.expand(sym.cos(x + y), trig=True))
# print(sym.cos(x) * sym.cos(y) - sym.sin(x) * sym.sin(y))
# print(sym.simplify((x**2 + x * y) / x))

# Exercises:
# 1. Calculate the expanded form of (x+y)^6
# 2. Simplify the trigonometric expression sin(x)/cos(x)

print(sym.expand((x+y)**6))
print(sym.simplify((sin(x)/cos(x)),trig=True))
