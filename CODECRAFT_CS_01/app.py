def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# -------- Main Program --------
def main():
    print("🔐 Caesar Cipher - Encrypt & Decrypt")
    print("------------------------------------")

    while True:
        print("\nChoose an option:")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plain_text = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value (e.g., 3): "))
            encrypted = encrypt(plain_text, shift)
            print("🔒 Encrypted Message:", encrypted)

        elif choice == '2':
            cipher_text = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value (e.g., 3): "))
            decrypted = decrypt(cipher_text, shift)
            print("🔓 Decrypted Message:", decrypted)

        elif choice == '3':
            print("Exiting... ✅")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
