from cryptography.fernet import Fernet

def create_key():
    #Generating encryption key
    #Keep this key secret
    key = Fernet.generate_key()
    print("Key: ", key.decode())
def encrypt(plain_text, key):
    #Convert plain_text and key into bytes for encryption
    plain_text = plain_text.encode()
    key = key.encode()
    #Encrypt data with key
    cipher_text = Fernet(key).encrypt(plain_text)
    #Convert cipher to text
    cipher_text = cipher_text.decode()
    return cipher_text

def decrypt(cipher_text, key):
    #Convert cipher_text and key into bytes
    cipher_text = cipher_text.encode()
    key = key.encode()
    #Decrypt the data
    plain_text = Fernet(key).decrypt(cipher_text)
    #Convert plain_text to string
    plain_text = plain_text.decode()
    return plain_text

encKey = ""

#Prompt user
method = ""
while method != "create key" and method != "encrypt" and method != "decrypt":
    method = input("Which would you like to do: create key, encrypt, decrypt: ")

print(method)
if method == "create key":
    create_key()
elif method == "encrypt":
    #Prompt user
    plain_text = input("Message to encrypt: ")
    encKey = input("Encryption key: ")
    #Call encryption function and print result
    cipher_text = encrypt(plain_text, encKey)
    print(cipher_text)
elif method == "decrypt":
    # Prompt user
    cipher_text = input("Message to decrypt: ")
    encKey = input("Encryption key: ")
    # Call encryption function and print result
    plain_text = decrypt(cipher_text, encKey)
    print(plain_text)

