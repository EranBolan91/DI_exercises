def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(ciphertext,shift):
    ciphertext = ciphertext.split()
    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)

    sentence = ' '.join(sentence)
    print('Decryption Successful\n')
    print ('Your encrypted sentence is:', sentence)

# --------------- Functions - end ---------------------- #

print("Hello User")
word = input("Please enter a word ")
answer = input("Would you like to encrypt the word? y/n ")

if(answer == 'y'):
    encrypt_word = encrypt(word,5)
    print('Word has been encrypted: ' + encrypt_word)

decrypt_answer = input("Would you like to decrypt your word? y/n ")
if decrypt_answer =='y':
    decrypt(encrypt_word,5)




