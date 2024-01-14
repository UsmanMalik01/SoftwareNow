def separate_and_convert(s):
    numbers = ''.join([c for c in s if c.isdigit()])
    letters = ''.join([c for c in s if c.isalpha()])
    
    even_numbers_ascii = [str(ord(c)) for c in numbers if int(c) % 2 == 0]
    upper_case_letters_ascii = [str(ord(c)) for c in letters if c.isupper()]
    
    return numbers, letters, even_numbers_ascii, upper_case_letters_ascii

def decrypt_cryptogram(cryptogram, shift):
    decrypted = ''
    for char in cryptogram:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted += char
    return decrypted

s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
numbers, letters, even_numbers_ascii, upper_case_letters_ascii = separate_and_convert(s)

print(f"Number String: {numbers}")
print(f"Letter String: {letters}")
print(f"Even Numbers (Original): {[int(c) for c in numbers if int(c) % 2 == 0]}")
print(f"Even Numbers (ASCII): {', '.join(even_numbers_ascii)}")
print(f"Upper-case Letters (Original): {[c for c in letters if c.isupper()]}")
print(f"Upper-case Letters (ASCII): {', '.join(upper_case_letters_ascii)}")

cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
for shift in range(26):
    decrypted = decrypt_cryptogram(cryptogram, shift)
    print(f"Shift {shift}: {decrypted}")
