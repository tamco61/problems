# 800
def func(word):
	f = word[0]
	l = word[-1]
	main = str(len(word[1:-1]))

	return f + main + l

n = int(input())

for i in range(n):
	word = input()

	if len(word) > 10:
		print(func(word))
	else:
		print(word)