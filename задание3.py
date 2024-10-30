import math
a = (2*math.pi)/6
v = 35
g = 9.81
x0 = -(math.tan(a)*2*v**2*math.cos(a)**2)/g
x0 = min(0, x0)
x0 = round(x0)
for i in range(x0*100, 10000, 1):
    x = 0.01*i
    y = x * math.tan(a) + ((g*x**2)/(2*v**2*math.cos(a)**2))
    if y > 0:
        print(x)
        break