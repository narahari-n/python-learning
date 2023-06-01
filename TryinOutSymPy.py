import sympy as sym
# Using sympy as a calculator

a = sym.Rational(1, 2)
print(a)
print(a*2)
print(sym.pi)
print(sym.pi**2)
print(sym.pi.evalf())
print(sym.exp(1).evalf())
print((sym.pi + sym.exp(1)).evalf())