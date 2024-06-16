def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - 97 + shift_amount) % 26 + 97)
            else:
                new_char = chr((ord(char) - 65 + shift_amount) % 26 + 65)
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - 97 - shift_amount) % 26 + 97)
            else:
                new_char = chr((ord(char) - 65 - shift_amount) % 26 + 65)
            decrypted_message += new_char
        else:
            decrypted_message += char
    return decrypted_message

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")

    if choice.lower() == 'e':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice.lower() == 'd':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
