from fractions import Fraction
import sympy

x= sympy.symbols("x")
f= sympy.Eq(x*Fraction('2/5'), 1760)
result= sympy.solve(f)
# print(result)

f= sympy.Eq(x**2, 7)
# print(sympy.solve(f))

x, y= sympy.symbols('x y')
f1= sympy.Eq(x+y, 10)
f2= sympy.Eq(x-y, 6)
print(sympy.solve([f1,f2]))

