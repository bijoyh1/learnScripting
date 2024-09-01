
def encoding():
    # Ask for rotation
    rotation = int(input("Enter the number of rotations you want? ")) % 26
    #Ask for plaintext
    plaintext = input("Enter plaintext: ")
    #Empty String
    encoded = ""
    new_location = 0
    #Loop through characters and apply rotation
    for i in plaintext:
        ascii_num = ord(i)
        if ascii_num > 90:
            location = ascii_num - 96
            new_location = 96
        else:
            location = ascii_num - 64
            new_location = 64
        new_location = new_location + ((location + rotation) % 26)
        if i == " ":
            encoded = encoded + " "
        else:
            encoded = encoded + str(chr(new_location))
    #Print encoded message
    print(encoded)


def decoding():
    rotation = int(input("Enter the number of rotations you want? ")) % 26
    ciphertext = input("Enter ciphertext ")
    decoded = ""
    new_location = 0
    for i in ciphertext:
       ascii_num = ord(i)
       if ascii_num > 90:
          location = ascii_num - 96
          new_location = 96
       else:
          location = ascii_num - 64
          new_location = 64
       new_location = new_location + ((location - rotation) % 26)
       if i == " ":
             decoded = decoded + " "
       else:
           decoded = decoded + str((chr(new_location)))

    # Print decoded message
    print(decoded)


encode = ""
# Encode or Decode
while encode != "encode" and encode != "decode":
    encode = input("Enter encode to encode a message or decode to decode a message: ")
if encode == 'encode':
    encoding()
else:
    decoding()
