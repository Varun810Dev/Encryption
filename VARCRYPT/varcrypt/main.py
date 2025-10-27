import os
import time
from colorama import Fore, Style, init
from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

# Fancy colored banner
BANNER = f"""
{Fore.GREEN}____   _________ __________________________________.___._____________________
\   \ /   /  _  \\______   \_   ___ \______   \__  |   |\______   \__    ___/
 \   Y   /  /_\  \|       _/    \  \/|       _//   |   | |     ___/ |    |   
  \     /    |    \    |   \     \___|    |   \\____   | |    |     |    |   
   \___/\____|__  /____|_  /\______  /____|_  // ______| |____|     |____|   
                \/       \/        \/       \/ \/                          

{Fore.CYAN}                 🔐 Varcrypt — Super Unicode Encryption 🔐
{Fore.MAGENTA}                     Created by Varun810Dev
{Style.RESET_ALL}
"""

# --- Character mapping for super encryption ---
ENCRYPT_MAP = {
    'a': 'à', 'b': 'β', 'c': 'ç', 'd': '∂', 'e': '€', 'f': 'ƒ',
    'g': 'ğ', 'h': 'ħ', 'i': 'į', 'j': 'ĵ', 'k': 'κ', 'l': 'ł',
    'm': '₥', 'n': 'η', 'o': 'ø', 'p': 'ρ', 'q': 'φ', 'r': 'я',
    's': 'š', 't': '†', 'u': 'ü', 'v': '√', 'w': 'ω', 'x': 'ж',
    'y': '¥', 'z': 'ž',
    '0': '⓪', '1': '①', '2': '②', '3': '③', '4': '④',
    '5': '⑤', '6': '⑥', '7': '⑦', '8': '⑧', '9': '⑨',
    ' ': '‣', '.': '•', ',': '‚', '!': '¡', '?': '¿'
}

# Reverse mapping for decryption
DECRYPT_MAP = {v: k for k, v in ENCRYPT_MAP.items()}


def encrypt(text: str) -> str:
    encrypted = []
    for char in text.lower():
        encrypted.append(ENCRYPT_MAP.get(char, char))
    return ''.join(encrypted)


def decrypt(text: str) -> str:
    decrypted = []
    for char in text:
        decrypted.append(DECRYPT_MAP.get(char, char))
    return ''.join(decrypted)


def show_progress(task_name="Processing", duration=2):
    print(Fore.MAGENTA + f"\n{task_name}...\n")
    for _ in tqdm(range(100), desc=Fore.CYAN + "Progress", ncols=75):
        time.sleep(duration / 100)
    print(Fore.GREEN + "✔ Done!\n")


def encrypt_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    show_progress("Encrypting file")
    encrypted_data = encrypt(data)

    output_path = file_path + ".enc.txt"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(encrypted_data)

    print(Fore.LIGHTGREEN_EX + f"🔒 File encrypted successfully and saved as: {output_path}")


def decrypt_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    show_progress("Decrypting file")
    decrypted_data = decrypt(data)

    output_path = file_path + ".dec.txt"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(decrypted_data)

    print(Fore.LIGHTBLUE_EX + f"🔓 File decrypted successfully and saved as: {output_path}")


def run():
    print(BANNER)
    print(Fore.YELLOW + "Choose:")
    print("1] Encrypt Text")
    print("2] Decrypt Text")
    print("3] Encrypt File")
    print("4] Decrypt File")

    choice = input(Fore.CYAN + "\nEnter your choice (1–4): " + Fore.WHITE).strip()

    if choice == '1':
        message = input(Fore.GREEN + "\nEnter the message you want to encrypt:\n> " + Fore.WHITE)
        show_progress("Encrypting text")
        encrypted_msg = encrypt(message)
        print(f"\n{Fore.LIGHTGREEN_EX}🔒 Encrypted message:\n{Fore.WHITE}{encrypted_msg}")

    elif choice == '2':
        message = input(Fore.BLUE + "\nEnter the message you want to decrypt:\n> " + Fore.WHITE)
        show_progress("Decrypting text")
        decrypted_msg = decrypt(message)
        print(f"\n{Fore.LIGHTBLUE_EX}🔓 Decrypted message:\n{Fore.WHITE}{decrypted_msg}")

    elif choice == '3':
        file_path = input(Fore.GREEN + "\nEnter file path to encrypt:\n> " + Fore.WHITE)
        if os.path.exists(file_path):
            encrypt_file(file_path)
        else:
            print(Fore.RED + "❌ File not found!")

    elif choice == '4':
        file_path = input(Fore.BLUE + "\nEnter file path to decrypt:\n> " + Fore.WHITE)
        if os.path.exists(file_path):
            decrypt_file(file_path)
        else:
            print(Fore.RED + "❌ File not found!")

    else:
        print(Fore.RED + "\n❌ Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    run()