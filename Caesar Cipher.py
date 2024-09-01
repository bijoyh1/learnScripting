rotation = int(input("Enter the number of rotations you want?"))
print(rotation)

test = 'Hello'

plaintext = input("Enter plaintext")
encoded = ""
for i in plaintext:
   encoded + str((chr(ord(i) + rotation)))



