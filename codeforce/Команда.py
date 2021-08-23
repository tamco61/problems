# 800
n = int(input())

lst = [sum([int(i) for i in input().split(' ')]) for r in range(n)]
n = 0
for i in lst:
	if i >= 2:
		n += 1
print(n)