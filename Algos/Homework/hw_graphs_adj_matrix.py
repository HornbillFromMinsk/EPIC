n, m = map(int, input().split(' '))
 
# Matrix 
Matrix = []

for _ in range(n):
	Matrix.append([0] * n)
 
for i in range(m):
	from_, to = map(int, input().split(' '))
	Matrix[from_ - 1][to - 1] = 1
 
for row in Matrix:
    print(*row, sep = ' ')