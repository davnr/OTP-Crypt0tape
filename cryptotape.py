import os
import argparse
import sys
import secrets
from datetime import datetime

def display_help():
    help_message = """
Crypt0tape - Mini Suite that uses OTP to encrypt messages
Credits: code written by dav_nr, algoritm used: OTP based on XOR

USAGE: python crypt0tape.py [command] <options>
NOTES: 
- Message.txt(s) and key.txt(s) can have any name, the important is that you put the exacxt name in the program
- For simplicity the program can operate with files that are placed in the same folder, so you can just put the name of the files after the commands

Commands:

[encrypt] <message.txt> <key.bin>
    Encrypts a txt file using the given key
    The message will be automatically saved with the name <nameOfTheTxtFile>.bin

[decrypt] <encrypted.bin> <key.bin>
    Decrypts a file and saves the result as a .txt file

[shred] <file>
    Destroys a .bin file in a safe way

[generate-key] <lenght>
    Generates a random OTP key with the given lenght in bytes

ATTENTION:
- OTP key must be as long as the message or longer
- NEVER use a key two times
- After using a key YOU MUST destroy it with shred, DON'T put it in the thrash bin
"""
    print(help_message)

def generate_key(length):
    key = secrets.token_bytes(length)
    hour = datetime.now().strftime("%H%M%S")
    path = "key" + hour + ".bin"
    write_file(path, key)
    print(f"[+] Key generated and saved with the name " + path)
    return key

def read_file(path):
    with open(path, 'rb') as f:
        return f.read()

def write_file(path, data):
    with open(path, 'wb') as f:
        f.write(data)

def xor_bytes(data1, data2):
    return bytes(a ^ b for a, b in zip(data1, data2))

def shred_file(path):
    try:
        length = os.path.getsize(path)
        with open(path, "wb") as f:
            f.write(secrets.token_bytes(length))
        os.remove(path)
        print(f"[+] {path} overwritten and removed.")
    except Exception as e:
        print(f"[!] Error during file's shredding: {e}")

def encrypt(message_path, key_path):
    message = read_file(message_path)
    key = read_file(key_path)

    if len(message) > len(key):
        print("[!] ERROR: the key must be as long as the message or longer")
        sys.exit(1)

    ciphertext = xor_bytes(message, key)
    base_name = os.path.splitext(os.path.basename(message_path))[0]
    output_path = base_name + ".bin"

    write_file(output_path, ciphertext)
    print(f"[+] File encrypted and saved as {output_path}")

def decrypt(cipher_path, key_path):
    cipher = read_file(cipher_path)
    key = read_file(key_path)

    if len(cipher) > len(key):
        print("[!] ERROR: The key must be as long or longer than the encrypted file")
        sys.exit(1)

    message = xor_bytes(cipher, key)
    base_name = os.path.splitext(os.path.basename(cipher_path))[0]
    output_path = base_name + ".txt"
    write_file(output_path, message)
    print(f"[+] File decrypted and saved as {output_path}")

def main():
    if len(sys.argv) == 1:
        display_help()
        sys.exit(0)

    parser = argparse.ArgumentParser(description="crypt0tape - Mini Suite that uses OTP to encrypt messages")
    subparsers = parser.add_subparsers(dest="command")

    enc = subparsers.add_parser("encrypt")
    enc.add_argument("message", help="File to Encrypt")
    enc.add_argument("key", help="OTP key")

    dec = subparsers.add_parser("decrypt")
    dec.add_argument("cipher", help="Encrypted file")
    dec.add_argument("key", help="Chiave OTP")

    shred = subparsers.add_parser("shred")
    shred.add_argument("file", help="File that has to be shred")

    gen_key = subparsers.add_parser("generate-key")
    gen_key.add_argument("length", type=int, help="Lenght of the key in bytes")

    args = parser.parse_args()

    if args.command == "encrypt":
        encrypt(args.message, args.key)
    elif args.command == "decrypt":
        decrypt(args.cipher, args.key)
    elif args.command == "shred":
        shred_file(args.file)
    elif args.command == "generate-key":
        generate_key(args.length)
    else:
        display_help()

if __name__ == '__main__':
    main()
