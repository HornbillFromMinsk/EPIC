'''
Extended Euclidean Algorithm
'''
def gcd_ext(a:int, b:int):
	if a == 0:
		return b, 0, 1
	gcd_res, x_new, y_new = gcd_ext(b % a, a)
	x, y = y_new - (b // a * x_new), x_new
	return gcd_res, x, y
 


if __name__=='__main__':
    a, b, c = map(int, input().split())

    gcd, x, y = gcd_ext(a, b)
    if c % gcd > 0:
        print('Impossible')
    else:
        print(gcd, x*c//gcd, y*c//gcd)