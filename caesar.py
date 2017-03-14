import string
alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

def alphabet_position(letter):
        letter = letter.lower()
        return alphabet[letter]

def rotate_character(char, rot):
	letters ='abcdefghijklmnopqrstuvwxyz'
	encrypted = ''
	if char.isalpha():
		l = char.lower()
		a = alphabet_position(l)
		rotated = a + rot
		if l in letters:
			if rotated < 26:
				if char.islower():
					encrypted = encrypted + letters[rotated]
				else:
					encrypted = encrypted + letters[rotated].upper()
			else:
				if char.islower():
					encrypted = encrypted + letters[rotated % 26]
				else: 
					encrypted = encrypted + letters[rotated % 26].upper()
	else:
		encrypted = encrypted + char
    
	return encrypted

def encrypt(text, rot):
	text = str(text)
	new_encrypt = ''
	for char in text:
		if char == ' ':
			new_encrypt += ' '
		else:
			new_encrypt += rotate_character(char, rot)
	return new_encrypt

def main():
	a = encrypt(input('Write a message:'),int( input('Rotate by:')))
	print(a)

if __name__ == '__main__':
	main()		
