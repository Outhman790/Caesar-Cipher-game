from logo import Logo
from functions import *
alphabet_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
isGameFinished = False

while isGameFinished == False:
    print(Logo)
    encode_or_decode = input("Type 'encode' to encrypt or type 'decode' to decrypt: \n")
    # Logic for encoding a word
    if encode_or_decode == "encode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: "))
        text_arr= list(text)
        encrypted_word_arr = []
        for letter in range(len(text_arr)):
            for i in range(len(alphabet_letters)):
                if text_arr[letter] == alphabet_letters[i]:
                    encrypted_word_arr.append(alphabet_letters[i+shift])
        print(f"{"".join(encrypted_word_arr)}")
        playAgain(isGameFinished)
       
    # Logic for decoding a word
    elif encode_or_decode == "decode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: "))
        text_arr= list(text)
        decrypted_word_arr = []
        for letter in range(len(text_arr)):
            for i in range(len(alphabet_letters)):
                if text_arr[letter] == alphabet_letters[i]:
                    decrypted_word_arr.append(alphabet_letters[i-shift])
        print(f"{"".join(decrypted_word_arr)}")
        playAgain(isGameFinished)

    # User wrote something different than encode or decode
    else:
        print("Please write either encode or decode")
        isGameFinished = False

  


