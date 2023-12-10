'''
Find such a number x
 that x^2+√X=C
, to an accuracy of at least 6 digits after the dot.
'''

EPS = 10 ** (-6)
 
def f(x):
	return (x * x) + (x ** (1/2))
 
def good(x, C):
	return f(x) - C < EPS
 
ops = 1000
C = 18.0000000000
l, r = -1, C
while ops > 0:
	mid = float (l + r) / 2
	if good(mid, C):
		l = mid
	else:
		r = mid
	ops -= 1
	
print(f"{l:.6f}")