import math
a = (2*math.pi)/6
v = 35
g = 9.81
for x in range(100, 100000000, 1):
    y = x * math.tan(a) + ((g*x**2)/(2*v**2*math.cos(a)**2))
    print(y/100)