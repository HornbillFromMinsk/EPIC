# Exponential search
x = 3
y = 4
n = 100
 
def good(t):
	return t * x + t * y < n
 
l = 0
r = 1
step = 1
 
while good(r):
	l = r
	r += step
	step *= 2
print(l, r)
 
while l < r - 1:
	mid = (l + r) // 2
	if good(mid):
		l = mid
	else:
		r = mid
 
print(l, r)