import math


def encrypt(key,text):
	numRows = int(math.ceil(len(text)/len(key)))
	numCols = len(key)
	mat = []

	# Frequency count
	chars = sorted(set(key))
	chrs = {}
	for i in chars:
		if i.isalpha():
			chrs[i] = key.count(i)

	mat.append([])
	tempKey = sorted(list(key))
	for i in range(numCols):
		tp = tempKey.index(key[i])
		mat[0].append(tp)
		tempKey[tp] = '$'


	for i in range(1,numRows+1):
		mat.append([])
		for j in range(numCols):
			mat[i].append('$')
	j = 0
	row = 1
	while j<len(text):
		for i in range(len(key)): 
			if j>= len(text):
				break
			mat[row][i] = text[j]
			j+=1
		row+=1
	# print(mat)
	encryptedMsg = ""
	for i in range(numCols):
		for j in range(numCols):
			if mat[0][j] == i:
				for k in range(1,numRows+1):
					encryptedMsg+=mat[k][j]
	# print(mat)
	return encryptedMsg


def decrypt(key,text):
	numRows = int(math.ceil(len(text)/len(key)))
	numCols = len(key)
	mat = []

	# Frequency count
	chars = sorted(set(key))
	chrs = {}
	for i in chars:
		if i.isalpha():
			chrs[i] = key.count(i)

	mat.append([])
	tempKey = sorted(list(key))
	for i in range(numCols):
		tp = tempKey.index(key[i])
		mat[0].append(tp)
		tempKey[tp] = '$'


	for i in range(1,numRows+1):
		mat.append([])
		for j in range(numCols):
			mat[i].append('$')

	curr = 0
	for i in range(numCols):
		for j in range(numCols):
			if mat[0][j] == i:
				for k in range(1,numRows+1):
					mat[k][j] = text[curr]
					curr+=1
	decryptMsg = ""
	for i in range(1,numRows+1):
		for j in range(numCols):
			decryptMsg+=mat[i][j]
	# print(mat)
	return decryptMsg


def subsEnc(sub,tex):
	tex2 = ""
	print(sub,tex)
	for i in tex:
		tex2+= chr(ord(i) + sub)

	return tex2

def subsDec(sub,tex):
	tex2 = ""
	for i in tex:
		tex2+= chr(ord(i) - sub)

	return tex2

key = "HACK"
text = "MYNAMEISSUSHANT"

key = int(input("Enter the cipher key: "))
text = input("Enter the plain text: ")
# num1 = int(input("Enter any number:")) 

enc = subsEnc(key,text)
print('Encrypted MSG:',enc)


enc = subsDec(key,enc).strip('$')
print('Decrypted MSG:',enc)
