def isPrime(n): 
    if n <= 1 : 
        return False
    for i in range(2, n): 
        if n % i == 0: 
            return False
  
    return True

def getPrimes(n):
    lst = []
    for i in range(2, n + 1): 
        if isPrime(i): 
            lst.append(i)
    return lst

def gcd(a,b): 
    if b==0:
        return a 
    else:
        return gcd(b,a%b)


def encryptt(no, e, n):
    encrypted = pow(no, e) % n
    print('Cipher Text = '+ str(encrypted))
    return encrypted

def decrypt(cipherdata, d, n):
    decrypted = pow(cipherdata, d) % n
    print('Decrypted Text = '+ str(decrypted))
    return decrypted


p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
no = int(input('Enter the value of text = ')) 
n = p*q

phi = (p-1)*(q-1)

print('n = ' + str(n))
print('phi = ' + str(phi))

e = 0
for ee in range(2,phi): 
    if gcd(ee,phi)== 1:
        print('Value of e (public key):' + str(ee))
        e = ee
        break
        

for i in range(1,phi): 
    x = 1 + i*phi 
    if x % e == 0: 
        d = int(x/e) 
        print('Value of d (private key):' + str(d))
        break


encrypted = encryptt(no, e, n)


decrypted = decrypt(encrypted, d, n)


# Factorisation Attack

def FA(n, e, cipherdata):
    primes = getPrimes(n)
    p1 = 0
    q1 = 0
    d1 = 0
    for i in primes:
        for j in primes:
            if i!=j :
                temp = i*j
                if(temp == n):
                    p1 = i
                    q1 = j
                    break;
                
    if(p1 == 0 and q1 == 0):
        print('No p and q found')
        return
    else:
        print('Found p and q')
        print('p: '+ str(p1) +' q:' + str(q1))
        phi = (p1-1)*(q1-1)
        for i in range(1,phi): 
            x = 1 + i*phi 
            if x % e == 0: 
                d1 = int(x/e) 
                break
        decrypt(cipherdata, d1, n) 
        print('RSA broken successfully')


cipherdata = int(input('Enter the value of cipherdata = ')) 
n = int(input('Enter the value of n = ')) 
e = int(input('Enter the value of e = ')) 


FA(n, e, cipherdata)

