from caesar import rotate_character
from caesar import alphabet_position

alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

def encrypt(text, word):
	n_encrypt = ''
	n_list = []
	z = 0
	for char in range(len(text)):
		for l in word:
			n_list.append(l)
	for char in text:
		keyletter = n_list[z]
		keyvalue = alphabet_position(keyletter)
		if char.isalpha() == True:
			x = rotate_character(char, keyvalue)
			n_encrypt += str(x)
			z += 1
		else:
			v = rotate_character(char, keyvalue)
			n_encrypt += str(v)
	return n_encrypt

def main():
	a = input('Type a message:')
	b = input('Encryption key:')
	x = encrypt(a, b)
	print(x)

if  __name__ == '__main__':
	main()
