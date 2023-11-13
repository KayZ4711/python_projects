# Lets create a password encryption program

import base64

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)

user_pass = input("Enter your password: ")
encrypt_pass(user_pass)

# Now lets create a password decryption program

def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decoded_data = decode_bytes.decode()
    print(f"decoded password {decoded_data}: ")

encode_string = input("enter the base64 string: ")
decode_pass(encode_string)

