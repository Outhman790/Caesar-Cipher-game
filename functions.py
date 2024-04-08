import subprocess
import os
import sys

def clear_screen():
    # Windows
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    # Mac and Linux
    else:
        subprocess.run('clear', shell=True)


def playAgain(isGameFinished):
    play_again = input("Type yes if you wanna play again, no for closing the game: ").lower()
    while play_again != "yes" and play_again != "no":
            play_again = input("Type yes if you wanna play again, no for closing the game: ").lower()
    if play_again == "yes":
            isGameFinished = False
            clear_screen()
    elif play_again == "no":
            isGameFinished = True
            sys.exit()
            

            

