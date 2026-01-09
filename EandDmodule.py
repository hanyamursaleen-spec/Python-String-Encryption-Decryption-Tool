import random
encrypt_shift = ["apple", "ball", "cat", "dog", "egg", "fish", "goat", "hat", "ice", "jam"]
print("Enter the text you want to encrypt:")
user_input = input(str).lower()
def encrypt(text):
    shift = random.randint(1,10) # Random shift between 1 and 10
    encrypted_text = ""
    for char in text:
        if char == " ":
            encrypted_text += " "
        elif chr(ord(char) + shift) > 'z':
            encrypted_text += chr((ord(char) + shift) - 26)  # Wrap around if past 'z'
        else:
            encrypted_text += chr(ord(char) + shift)  # Shift character by a random number
    #encrypt the shift value with the text
    out_val = encrypt_shift[shift]
    return encrypted_text, out_val
print("Encrypted text:", encrypt(user_input))

print("Enter the text you want to decrypt:")
user_input_decrypt = input(str)
print("Enter the shift value you received during encryption:")
out_val = input(str)
def decrypt(text, out_val):
    decrypted_text = ""
    shift = encrypt_shift.index(out_val)
    for char in text:
        if char == " ":
            decrypted_text += " "
        elif chr(ord(char) - shift) < 'a':
            decrypted_text += chr((ord(char) - shift) + 26)  # Wrap around if before 'a'
        else:
            decrypted_text += chr(ord(char) - shift)  # Shift character back by the same number
    return decrypted_text
print("Decrypted text:", decrypt(user_input_decrypt, out_val))