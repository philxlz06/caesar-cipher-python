def caeser_cipher(message, shift, encode=True):
    result = ""

    if not encode:
        shift = -shift

    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
    else:
        result += char
    return result


def main():
    while True:
        print("\n=== Caeser Cipher Encoder/Decoder ===")
        message = input("Enter your message: ")

        while True:
            try:
                shift = int(input("enter shift number(1-25): ")) % 26
                break
            except ValueError:
                print("Please enter a valid number. ")

        choice = input("Do you want to (E)ncode or (D)ncode? ").strip().lower()
        encode = choice == 'e'

        result = caeser_cipher(message, shift, encode)
        print(f"{'Encoded' if encode else 'Decoded '} message: {result}")

        again = input("Do you want to try again? (Y/N): ").strip().lower()
        if again != 'y':
         print("Goodbye!")
         break


if __name__ == "__main__":
    main()
