import sympy as sym
import os #For clearing the terminal (or console) screen everytime by calling os.system('cls')

a = sym.Rational(1, 2)
os.system('cls')    #This is equivalent to clrscr() in c or clc in MATLAB.

""" # Using sympy as a calculator
print(a)
print(a*2)
print(sym.pi)
print(sym.pi**2)
print(sym.pi.evalf())
print(sym.exp(1).evalf())
print((sym.pi + sym.exp(1)).evalf())

b = (sym.oo > 99999999) #sym.oo is infinity
print(b)
print(sym.oo+1)     #infinity+1 is also infinity """

""" Exercises

Calculate \sqrt{2} with 100 decimals.
Calculate 1/2 + 1/3 in rational arithmetic. """



num1 = sym.Rational(1,2)
num2 = sym.Rational(1,3)
print(num1+num2)
