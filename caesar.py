import string

def alphabet_position(letter):
	'''takes char letter
	returns its position in the alphabet, regardless of caps'''
	if letter.islower():
		return string.ascii_lowercase.find(letter)
	elif letter.isupper():
		return string.ascii_uppercase.find(letter)
	else:
		return None
		
def rotate_character(char, rot):
	'''takes char char and int rot
	returns new char based off new rot position in a caesar cypher'''
	currpos = alphabet_position(char)
	if currpos is not None:
		pos = (currpos + rot) % 26

	if char.islower():
		return string.ascii_lowercase[pos]
	elif char.isupper():
		return string.ascii_uppercase[pos]
	else:
		return char

def encrypt(text, rot):
	'''takes str text and int rot
	returns caesar encrypted text by rot position'''
	newtext = []
	for char in text:
		newtext.append(rotate_character(char, rot))
	return "".join(newtext)
