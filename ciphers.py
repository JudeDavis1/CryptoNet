import random


class CipherHandler:

    def __init__(self, random_prime=True, p=0, q=0):
        self.p = p
        self.q = q
        self.public_key = None
        self.private_key = None
        self.plaintext = None
        self.ciphertext = None

        # keep generating a random number until it is prime
        if random_prime:
            while not self._is_prime(self.p) or not self._is_prime(self.q) and self.q == self.q:
                self.p = random.randint(100, 500)
                self.q = random.randint(100, 500)

    # greatest common divisor
    def _GCD(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # checks if number is a prime number
    def _is_prime(self, n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False

        for i in range(3, int(n ** 0.5) + 2, 2):
            if n % i == 0:
                return False

        return True

    def _modulo_inverse(self, a, m):
        a = a % m
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return 1

    # generates a public and private key
    def keypair_gen(self):
        p = self.p
        q = self.q

        if not (self._is_prime(p) and self._is_prime(q)):
            raise ValueError("Both numbers have to be prime.")
        elif p == q:
            raise ValueError("Both numbers cannot be equal.")

        N = p * q  # N = pq
        phi = (p - 1) * (q - 1)  # phi is the totient of n
        e = random.randrange(1, phi)
        g = self._GCD(e, phi)

        while g != 1:
            e = random.randrange(1, phi)
            g = self._GCD(e, phi)

        d = self._modulo_inverse(e, phi)
        # ((public key), (private key))
        self.public_key = (e, N)
        self.private_key = (d, N)

    # encrypt plaintext given a public key and return cipher
    def encrypt(self, plaintext):
        key, N = self.public_key
        self.ciphertext = [(ord(char) ** key) % N for char in plaintext]

    # decrypt cipher given a private key and return plaintext
    def decrypt(self, ciphertext):
        key, N = self.private_key
        pure_text = [chr((char ** key) % N) for char in ciphertext]

        return ''.join(pure_text)
