import random

class Merkle_Hellman_Cipher:
    def __init__(self):
        self.word = ""
        self.private_key = []
        self.public_key = []
        self.vec_str = []
        self.vector_encryption = []
        self.dec_vec = []
        self.decimalValues = []
        self.q = 0
        self.r = 0
        self.r_shtix = 0

    def to_binary(self, decimal):
        binary = bin(decimal)[2:] 
        binary = binary.zfill(7)  
        return binary

    def number_is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def initialize_vector(self):
        for i in range(8):
            self.private_key.append(2 ** i)

    def initialize_R(self):
        self.r = random.randint(1, 100)
        while not self.number_is_prime(self.r):
            self.r = random.randint(1, 100)
        return self.r

    def initialize_Q(self):
        self.q = random.randint(0, 100) + self.private_key[-1]
        return self.q
    
    def set_word(self):
        import os
        self.word = os.getenv("var1")

    def get_word(self):
        return self.word

    def set_string_vector(self):
        for i in range(len(self.get_word())):
            self.vec_str.append(self.to_binary(ord(self.get_word()[i])))

    def generate_public_key(self):
        for c in self.private_key:
            self.public_key.append(c * self.r % self.q)

    def encrypt(self):
        for str in self.vec_str:
            sum = 0
            for i in range(len(str)):
                if str[i] == '1':
                    sum += self.public_key[i]
            self.vector_encryption.append(sum)

    def decrypt(self):
        self.r_shtix = self.multiplicative_inverse(self.r, self.q)
        self.private_key.sort(reverse=True)

        temp = []
        for i in self.vector_encryption:
            temp.append(i * self.r_shtix % self.q)

        for i in range(len(temp)):
            index = ""
            while temp[i] != 0:
                for c in range(len(self.private_key)):
                    if c == 0:
                        continue
                    if temp[i] < self.private_key[c]:
                        index += "0"
                        continue
                    else:
                        index += "1"
                        temp[i] -= self.private_key[c]
                index = index[::-1]
                self.dec_vec.append(index)

        self.binary_to_decimal(self.dec_vec)

    def gcd_extended(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    def multiplicative_inverse(self, a, m):
        gcd, x, y = self.gcd_extended(a, m)
        if gcd != 1:
            return -1
        else:
            return (x % m + m) % m

    def binary_to_decimal(self, binaryValues):
        for binary in binaryValues:
            decimal = 0
            base = 1
            for i in range(len(binary) - 1, -1, -1):
                if binary[i] == '1':
                    decimal += base
                base *= 2
            self.decimalValues.append(decimal)

    def show_result(self):
        print("Q: ", self.q)
        print("R: ", self.r)
        print("R': ", self.r_shtix)
        print("Приватный ключ: ", self.private_key)
        print("Публичный ключ: ", self.public_key)
        print("Слово в двоичном формате: ", self.vec_str)
        print("Зашифрованное слово: ", self.vector_encryption)
        print("Расшифрованное слово: ", ''.join([chr(c) for c in self.decimalValues]))
