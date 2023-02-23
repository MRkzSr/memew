import random
import math

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    if not(is_prime(p) and is_prime(q)):
        raise ValueError("Kedua bilangan harus prima.")
    elif p == q:
        raise ValueError("p dan q tidak boleh sama.")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = modinv(e, phi)
    return ((n, e), (n, d))

def modinv(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x

def encrypt(pk, plaintext):
    n, e = pk
    cipher = [pow(ord(char),e,n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    n, d = pk
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = 17
    q = 19
    public, private = generate_keypair(p, q)
    print("Kunci publik: ", public)
    print("Kunci privat: ", private)
    message = "Hello, world!"
    encrypted_message = encrypt(public, message)
    print("Pesan terenkripsi: ", ''.join(map(lambda x: str(x), encrypted_message)))
    decrypted_message = decrypt(private, encrypted_message)
    print("Pesan terdekripsi: ", decrypted_message)
