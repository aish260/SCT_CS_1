def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result


message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))
action = input("Choose action - 'encrypt' or 'decrypt': ").strip().lower()


if action in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift_value, action)
    print(f"\nYour {action}ed message: {output}")
else:
    print("Invalid action! Please choose 'encrypt' or 'decrypt'.")
