
from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt(key, pwd):
    cipher_suite = Fernet(key)
    bpwd = bytes(pwd, 'utf-8')
    ciphered_text = cipher_suite.encrypt(bpwd)
    return ciphered_text


def decrypt(key, enc_pwd):
    cipher_suite = Fernet(key)
    uncipher_text = (cipher_suite.decrypt(enc_pwd))
    return bytes(uncipher_text).decode("utf-8")

key = generate_key()
print(bytes(key).decode("utf-8"))
encryptstr = encrypt(key, "abc123")
print(bytes(encryptstr).decode("utf-8"))
print(decrypt(key, encryptstr))