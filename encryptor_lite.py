from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import sys
import os

def encrypt_file(key, filename):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(filename, 'rb') as f:
        original_data = f.read()
    encrypted_data = cipher.encrypt(pad(original_data, AES.block_size))
    with open(filename, 'wb') as f:
        f.write(cipher.iv)
        f.write(encrypted_data)

def decrypt_file(key, filename):
    with open(filename, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    with open(filename, 'wb') as f:
        f.write(original_data)

def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ")
    filename = input("Please enter the full path to the file: ")
    key = input("Please enter your 16, 24, or 32 byte key: ")
    if choice.lower() == 'e':
        encrypt_file(key.encode(), filename)
    elif choice.lower() == 'd':
        decrypt_file(key.encode(), filename)
    else:
        print("Invalid option, please choose (E)ncrypt or (D)ecrypt.")

if __name__ == '__main__':
    main()