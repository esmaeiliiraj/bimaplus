# Polygon Characteristics


# Getting inputs========================================

n = int(input ('Enter the number of points: '))

x = []
y = []

print()
print ('Enter the x and y coordinates for the polygon points ...')
print()

for i in range(n):
    xInput = float (input(f'x{i + 1}: '))
    yInput = float (input(f'y{i + 1}: '))
    
    x.append(xInput)
    y.append(yInput)

print()


# Table of points and coordinates=======================

print(f'{"Point":10} {"x":11} {"y":10}')
print('-' * 30)    

for i in range(n):
    print(f'{i+1} {x[i]:11} {y[i]:11}')


# Geometric charactristics calculations=================

print()
print('Geometric Characteristics:')
print()

s1 = 0
for i in range(n):
    a = x[i] + x[i-1]
    b = y[i] - y[i-1]
    m = a * b
    s1 = s1 + m

Ax = 0.5 * s1
print (f'{"Ax:":6} {Ax:15.2f}')

s2 = 0
for i in range(n):
    a = x[i] - x[i-1]
    b = y[i]**2 + y[i] * y[i-1] + y[i-1]**2
    m = a * b
    s2 = s2 + m

Sx = -(1/6) * s2
print(f'{"Sx:":6} {Sx:15.2f}')

s3 = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = x[i]**2 + x[i] * x[i-1] + x[i-1]**2
    m = a * b
    s3 = s3 + m

Sy = (1/6) * s3
print(f'{"Sy:":6} {Sy:15.2f}')

s4 = 0
for i in range(n):
    a = x[i] - x[i-1]
    b = y[i]**3 + (y[i]**2) * y[i-1] + y[i] * (y[i-1]**2) + y[i-1]**3
    m = a * b
    s4 = s4 + m
    
Ix = -(1/12) * s4
print(f'{"Ix:":6} {Ix:15.2f}')

s5 = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = x[i]**3 + (x[i]**2) * x[i-1] + x[i] * (x[i-1]**2) + x[i-1]**3
    m = a * b
    s5 = s5 + m
    
Iy = (1/12) * s5
print(f'{"Iy:":6} {Iy:15.2f}')

s6 = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = (y[i] * (3 * x[i]**2 + 2 * x[i] * x[i-1] + x[i-1]**2)) + y[i-1] * (3 * x[i-1]**2 + 2 * x[i] * x[i-1] + x[i]**2)
    m = a * b
    s6 = s6 + m
    
Ixy = -(1/24) * s6
print(f'{"Ixy:":6} {Ixy:15.2f}')

xt = Sy / Ax
print(f'{"xt:":6} {xt:15.2f}')

yt = Sx / Ax
print(f'{"yt:":6} {yt:15.2f}')

Ixt = Ix - (yt**2) * Ax
print(f'{"Ixt:":6} {Ixt:15.2f}')

Iyt = Iy - (xt**2) * Ax
print(f'{"Iyt:":6} {Iyt:15.2f}')

Ixyt = Ixy + xt * yt * Ax
print(f'{"Ixyt:":6} {Ixyt:15.2f}')
    
