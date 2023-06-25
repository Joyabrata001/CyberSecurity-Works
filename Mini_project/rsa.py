import random

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]
                     
def modular(a, m, n):
    d = 0
    bin_num =  int(bin(m).replace("0b", ""))
    length = len(bin(m).replace("0b", ""))
    last_digit = bin_num%10
    index = 0
    res = 1
    while bin_num>0:
        power = pow(2, index)
        if index == 0:
            d = a%n
        else:
            d = (d*d)%n
        last_digit = bin_num%10
        if last_digit == 1:
            res = (res*d)%n
        bin_num = bin_num//10
        index = index + 1

    return res
    
def mulinverse(r2, r1):
    t1 = 0
    t2 = 1
    n = r1
    while(r2>0):
        q = r1//r2
        t = t1 - q*t2
        r = r1%r2
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t
    
    if t1<0:
        return t1+n
    return t1

def computeGCD(x, y):
    while(y):
        x, y = y, x%y
    return abs(x)

def nBitRandom(n):
    return random.randrange(2**(n-1) +1, 2**n-1)

def getLowLevelPrime(n):
    while True:
        pc = nBitRandom(n)

        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
            else:
                return pc

def trialPrime(round_tester, ec, mrc, maxDivisonsByTwo):
    b = modular(round_tester, ec, mrc)
    b1 = 0
    if b == 1 or b == -1:
        return True
    if maxDivisonsByTwo == 1:
        return False
    else:
        for r in range(1, maxDivisonsByTwo-1):
            b1 = modular(b, 2, mrc)
            if b1 == -1:
                return True
            elif b1 == 1:
                return False
        res = modular(b1, 2, mrc)
        if res == -1:
            return True
        else:
            return False

def isMillerRabinPassed(mrc):
    maxDivisonsByTwo = 0
    ec = mrc -1
    while ec%2 == 0:
        ec >>=1
        maxDivisonsByTwo += 1
    numberofMillerRabinTrials = 20
    for i in range(numberofMillerRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialPrime(round_tester, ec, mrc, maxDivisonsByTwo):
            return True
        return False

def generatedPrime(n):
    prime_candidate = getLowLevelPrime(n)
    while not isMillerRabinPassed(prime_candidate):
        prime_candidate = getLowLevelPrime(n)
    return prime_candidate

def rsaKeys(keySize):
    p = generatedPrime(keySize)
    q = generatedPrime(keySize)
    n = p*q
    phi = (p-1)*(q-1)
#    print(phi)
    e = random.randint(1, phi)
    while(computeGCD(e, phi) != 1):
        e = random.randint(1, phi)
    d = mulinverse(e, phi)
    return e, d, n

if __name__ == '__main__':
    
    e, d, n = rsaKeys(1024)

    plaintext = input("Enter plaintext: ")

    # Converting plaintext to integer
    plain_int = int.from_bytes(plaintext.encode(), 'big')

    cipher_int = modular(plain_int, e, n)

    # Converting ciphertext to bytes and write to file
    with open('encrypted.txt', 'wb') as f:
        f.write(cipher_int.to_bytes((cipher_int.bit_length() + 7) // 8, 'big'))

    with open('encrypted.txt', 'rb') as f:
        cipher_bytes = f.read()
    cipher_int = int.from_bytes(cipher_bytes, 'big')
    decrypted_int = modular(cipher_int, d, n)

    # Converting decrypted integer to plaintext and write to file
    decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big')
    with open('decrypted.txt', 'w') as f:
        f.write(decrypted_bytes.decode())
