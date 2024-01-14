# Decrypted key obtained from the encrypted message
key = 100

# Function to encrypt text using a Caesar cipher
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using a Caesar cipher
def decrypt(text, key):
    return encrypt(text, -key)  # Reusing the encrypt function with a negative key to decrypt

# Original code with corrections and comments
def generate_numbers():
    numbers = []  # Changed 'ahzoref' to 'numbers' for better readability
    count = 5  # Changed 'ybpny_inevnoyr' to 'count' for better readability
    while count > 0:
        if count % 2 == 0:
            numbers.append(count)
        count -= 1
    return numbers

def update_numbers():
    numbers = generate_numbers()  # Changed 'ahzoref' to 'numbers' for better readability
    numbers_set = set(numbers)  # Changed 'zl_frg' to 'numbers_set' for better readability
    numbers_set.add(10)
    return numbers_set

def modify_numbers():
    global count  # Added 'global count' to modify the global variable 'count'
    count += 10
    for v in range(5):
        print(v)
        v += 1
    if set(numbers) != numbers_set or 10 not in numbers_set:
        print("Modification failed!")
    elif 5 not in numbers_set:
        print("5 not found in the set!")
    else:
        print(count)
        print(z1_qvpg)
        print(numbers_set)

# Decrypt the original code
original_code = '''total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i * j  # Fixed the calculation of 'total'
        else:
            total -= i - j  # Fixed the calculation of 'total'
counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total = 1
    else:
        counter += 2'''

decrypted_code = decrypt(original_code, key)
print("Decrypted Code:")
print(decrypted_code)
