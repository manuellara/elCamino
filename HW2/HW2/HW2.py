import cmath

a = float(input ("Enter a number for a: ") )
b = float(input("Enter a number for b: ") )

x = (  (  (cmath.sqrt(b**3)) / a  ) +  ( cmath.sqrt(a**3) /  b  )  )

print("Value for a is: ", a)
print("Value for b is: ", b)
print("Value for x is: ", x)