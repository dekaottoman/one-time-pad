import random

def generateKey(path:str):
    f = open(path, 'rb')
    file = f.read()
    f.close()
    key = random.randbytes(len(file))
    print(key)
    print(len(file))
    print(len(key))
    f = open(path + '.key', 'wb')
    f.write(key)
    f.close()

def encrypt(keyPath:str,filePath:str):
    f = open(filePath, 'rb')
    file = f.read()
    f.close()

    k = open(keyPath, 'rb')
    key = k.read()
    k.close

    file = bytearray(file)
    key = bytearray(key)
    for i, f in enumerate(file):
        file[i] = f^key[i]

    fenc = open(filePath + ".enc", 'wb')
    fenc.write(file)
    fenc.close()
    print('Encryption Done...')

def decrypt(key_path:str,file_path:str):
    f = open(file_path, 'rb')
    file = f.read()
    f.close()

    k = open(key_path, 'rb')
    key = k.read()
    k.close

    file = bytearray(file)
    key = bytearray(key)
    for i, f in enumerate(file):
        file[i] = f^key[i]

    fenc = open(file_path.replace(".enc", ""), 'wb')
    fenc.write(file)
    fenc.close()
    print('Decryption Done...')

if __name__ == '__main__':
    while True:
        command = input("Enter command :\n-keyGen\n-encrypt\n-decrypt\n-exit\ncommand >> ")
        if command == "keyGen":
            path = input("Enter path : ")
            generateKey(path)
        elif command == "encrypt":
            filePath = input("Enter file path : ")
            keyPath = input("Enter key path : ")
            encrypt(keyPath, filePath)
        elif command == "decrypt":
            filePath = input("Enter enc file path : ")
            keyPath = input("Enter key path : ")
            decrypt(keyPath, filePath)
        elif command == "exit":
            exit(0)