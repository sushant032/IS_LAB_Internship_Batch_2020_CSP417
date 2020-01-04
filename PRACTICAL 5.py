from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as tkMessageBox
import os


from PIL import Image
import math
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import hashlib
import binascii


# ### DES Algorithm for image Encryption

def encrypt(imagename,password,iv):

    plaintext = list()
    plaintextstr = ""


    im = Image.open(imagename)
    pix = im.load()

    
    width = im.size[0]
    height = im.size[1]

    
    for y in range(0,height):
        for x in range(0,width):
            plaintext.append(pix[x,y])

    
    for i in range(0,len(plaintext)):
        for j in range(0,3):
            plaintextstr = plaintextstr + "%d" %(int(plaintext[i][j])+100)

    
    relength = len(plaintext)

    plaintextstr += "h" + str(height) + "h" + "w" + str(width) + "w"

    while (len(plaintextstr) % 16 != 0):
        plaintextstr = plaintextstr + "n"

    
    key=password.encode('utf-8')
    des1 = DES.new(key, DES.MODE_CFB, iv)

    plainText=plaintextstr.encode('utf-8')
    ciphertext = des1.encrypt(plainText)
    print("CIPHER TEXT CREATED ....")
    cipher_name = imagename + ".crypt"
    g = open(cipher_name, 'wb')
    g.write(ciphertext)

    def construct_enc_image():
        asciicipher = binascii.hexlify(ciphertext)
        def replace_all(text, dic):
            for i, j in dic.items():
                text = text.replace(i, j)
            return text

        reps = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}
        asciicipher=asciicipher.decode('utf-8')
        asciiciphertxt = replace_all(asciicipher, reps)

        step = 3
        encimageone=[asciiciphertxt[i:i+step] for i in range(0, len(asciiciphertxt), step)]
        if int(encimageone[len(encimageone)-1]) < 100:
            encimageone[len(encimageone)-1] += "1"
        if len(encimageone) % 3 != 0:
            while (len(encimageone) % 3 != 0):
                encimageone.append("101")

        encimagetwo=[(int(encimageone[int(i)]),int(encimageone[int(i+1)]),int(encimageone[int(i+2)])) for i in range(0, len(encimageone), step)]

        while (int(relength) != len(encimagetwo)):
            encimagetwo.pop()

        encim = Image.new("RGB", (int(width),int(height)))
        encim.putdata(encimagetwo)

        encim.show()

    construct_enc_image()


def decrypt(ciphername,password,iv):
    cipher = open(ciphername,'rb')
    ciphertext = cipher.read()

    key=password.encode('utf-8')
    des2 = DES.new(key, DES.MODE_CFB, iv)

    decrypted=des2.decrypt(ciphertext)

    decrypted=decrypted.decode('utf-8')

    decrypted = decrypted.replace("n","")

    newwidth = decrypted.split("w")[1]
    newheight = decrypted.split("h")[1]

    heightr = "h" + str(newheight) + "h"
    widthr = "w" + str(newwidth) + "w"
    decrypted = decrypted.replace(heightr,"")
    decrypted = decrypted.replace(widthr,"")

    step = 3
    finaltextone=[decrypted[i:i+step] for i in range(0, len(decrypted), step)]
    finaltexttwo=[(int(finaltextone[int(i)])-100,int(finaltextone[int(i+1)])-100,int(finaltextone[int(i+2)])-100) for i in range(0, len(finaltextone), step)]

    newim = Image.new("RGB", (int(newwidth), int(newheight)))
    newim.putdata(finaltexttwo)
    newim.show()


def imageEncryption(filename, password,iv):
    file_path_e = os.path.dirname(filename)
    print("ENCRYPTING...")
    encrypt(filename,password,iv)
    print("FILE SUCCESSFULLY ENCRYPTED.... ")


def imageDecryption(filename, password,iv):
    file_path_d = os.path.dirname(filename)
    decrypt(filename,password,iv)
    print("FILE SUCCESSFULLY DECRYPTED.... ")


from Crypto import Random
iv = Random.get_random_bytes(8)




filename = r"0.jpg"
imageEncryption(filename, "HORSES",iv) 

cipherfile = r"0.jpg.crypt"
imageDecryption(cipherfile, "HORSES",iv)




# ### DES with CFB for TEXT


from Crypto.Cipher import DES
from Crypto import Random


def pad(text):
    while len(text)%8!=0:
        text+=" "
    return text



iv = Random.get_random_bytes(8)

des1 = DES.new(b'01234567', DES.MODE_CFB, iv)

des2 = DES.new(b'01234567', DES.MODE_CFB, iv)

file = "input.txt"
with open(file) as f:
    text = f.read().strip()
    text = text.lower()


text = pad(text)
text = str.encode(text)

cipher_text = des1.encrypt(text)

decipher_text=des2.decrypt(cipher_text)


print(cipher_text)

print(decipher_text)


# ### DES with OFB for TEXT


iv = Random.get_random_bytes(8)

des1 = DES.new(b'01234567', DES.MODE_OFB, iv)

des2 = DES.new(b'01234567', DES.MODE_OFB, iv)

file = "input.txt"
with open(file) as f:
    text1 = f.read().strip()
    text1 = text1.lower()

text1 = pad(text1)
text1 = str.encode(text1)

cipher_text = des1.encrypt(text1)

decipher_text=des2.decrypt(cipher_text)

print(cipher_text)

print(decipher_text)
