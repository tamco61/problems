import string

def rot13(message):
	alphabet = string.ascii_lowercase
	new_message = ''
	for s in message:
		i = alphabet.index(s)
		if i - 13 < 0:
			i = abs(i - 12) + 1
		else:
			i -= 13
		new_message += alphabet[i]

	return new_message
print(rot13('a'))