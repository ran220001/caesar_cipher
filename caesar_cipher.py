# Caesar cipher (with algorithm learned from discrete mathematics)
# January 1, 2023

default_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher(plaintext, offset, letters = default_letters):
    ciphertext = ''
    for x in plaintext:
        index = letters.find(x.upper())
        if index >= 0:
            ciphertext += letters[(index + offset) % 26]
        else:
            ciphertext += x
    return ciphertext

if __name__ == '__main__':
    input_plaintext = input("Enter a sentence: ")
    input_offset = int(input("Enter offset: "))

    output_ciphertext = caesar_cipher(input_plaintext, input_offset)

    print(output_ciphertext)
