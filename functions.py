import subprocess
import os
import sys
alphabet_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# A function asking the user if he wants to play again 
def playAgain(isGameFinished):
    play_again = input("Type yes if you wanna play again, no for closing the game: ").lower()
    while play_again != "yes" and play_again != "no":
            play_again = input("Type yes if you wanna play again, no for closing the game: ").lower()
    if play_again == "yes":
            isGameFinished = False
            # Clear screen and play again
            clear_screen()
    elif play_again == "no":
            isGameFinished = True
            # Close the game in terminal
            sys.exit()
            

def ceaserCipher(encodeordecode,isGameFinished):
        if encodeordecode == "encode" or encodeordecode == "decode":
            text = input("Type your message: \n").lower()
            shift = int(input("Type the shift number: "))
            text_arr= list(text)
            ceaserCipher_word_arr = []
            if shift >= len(alphabet_letters):
                 shift = shift % len(alphabet_letters)
                 print(f"Hhere is shift value {shift}")
            shift = -shift if encodeordecode == "decode" else shift
            for letter in range(len(text_arr)):
                for i in range(len(alphabet_letters)):
                    if text_arr[letter] == alphabet_letters[i]:
                        ceaserCipher_word_arr.append(alphabet_letters[(i+shift) % len(alphabet_letters)])
            print(f"{"".join(ceaserCipher_word_arr)}")
            playAgain(isGameFinished)
        else:
           print("Please write either encode or decode")
           isGameFinished = False

# A function for cleaning terminal screen
def clear_screen():
    # Windows
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    # Mac and Linux
    else:
        subprocess.run('clear', shell=True)


            

