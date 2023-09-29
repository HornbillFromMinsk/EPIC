'''
Find such a number x
 that x^2+√X=C
, to an accuracy of at least 6 digits after the dot.
'''

EPS = 10 ** (-6)
 
def f(x, C):
	return (x * x) - (x ** (1/2)) - C
 
def good(x, C):
	return f(x, C) - f(x - EPS, C) <= 0
 
l, r = 0, 100
ops = 100
C = 2.0000000000
while ops > 0:
	mid = float (l + r) / 2
	if good(mid, C):
		l = mid
	else:
		r = mid
	ops -= 1
print(l, r)