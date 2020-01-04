def generate_key(message, key):
    i = 0
    while True:
        if len(key) == len(message):
            break
        if message[i] == ' ':
            i += 1
        else:
            key += message[i] 
            i += 1
    return key

def encryptWithAutoKey(message, key_new):
    cipher_text = ''
    i = 0
    for letter in message:
        if letter == ' ':
            cipher_text += ' '
        else:
            x = (ord(letter.upper())-65+ord(key_new[i].upper())-65) % 26 
            i += 1
            cipher_text += chr(x+65) 
    return cipher_text 

def decryptWithAutoKey(cipher_text, key_new):
    decrypt_txt = ''
    i = 0
    for letter in cipher_text:
        if letter == ' ':
            decrypt_txt += ' '
        else:
            x = (ord(letter.upper())-65-ord(key_new[i].upper())-65+26) % 26 
            i += 1
            decrypt_txt += chr(x+65) 
    return decrypt_txt



message = input('Enter the text to be encrypted: ')
key = input('Enter the key: ')
key_new = generate_key(message, key)
print('Key:',key_new)
encrypted_text = encryptWithAutoKey(message, key_new)
decrypted_text = decryptWithAutoKey(encrypted_text, key_new)

print("Encrypted Text =", encrypted_text)

print("Decrypted Text =", decrypted_text)




import random, string

message = input('Enter the text to be encrypted: ')


key = ''.join(random.choice(string.ascii_uppercase) for x in range(len(message)))
print('Key:',key)

encrypted_text = encryptWithAutoKey(message, key)
decrypted_text = decryptWithAutoKey(encrypted_text, key)

print("Encrypted Text =", encrypted_text)
print("Decrypted Text =", decrypted_text)

