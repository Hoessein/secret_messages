import os

from atbash import Atbash
from keywrd import Keyword
from affine import Affine
import sys


def instructions():
    """These are a couple of printed statement for the user
        so they know what to expect and which instructions to follow
    """
    print("This is the secret messages project for Treehouse.\n"
          "\nThese are the current available ciphers:\n"
          "\nPress 1 for the Affine Cipher"
          "\nPress 2 for the Atbash Cipher"
          "\nPress 3 for the Keyword Cipher")


def clear():
    """This is a function that clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    """this is a function where i run the game logic
        ask the user if they want to play again
        if so the secret messages will run again
        otherwise the user is thanked and the program shuts down"""
    run_cipher()
    play_again = input("\nEnter 'Y' if you want to use the program again, Enter anything else to quit. ")
    play_again = play_again.upper()
    clear()
    while True:
        if play_again == 'Y':
            instructions()
            game()
        else:
            print("Thank you for using secret messages!")
            break
    sys.exit(0)

def run_cipher():
    """prompts the user which cipher they would like
        if the user input matches a cipher that particular cipher method will run
        the while loop will keep prompting the user to pick an available cipher
    """
    while True:
        which_cipher = input("\nWhich cipher would you like to use?: ")
        if which_cipher == '1':
            run_affine_cipher()
            break
        elif which_cipher == '2':
            run_atbash_cipher()
            break
        elif which_cipher == '3':
            run_keyword_cipher()
            break
        else:
            print("\nThat choice is not available, try again please! ")

def run_affine_cipher():
    """this method prompts the user if they would like to encrypt or decrypt
    and runs the encrypt or decrypt method of this cipher
    """
    affine = Affine()
    while True:
        encrypt_decrypt = input("\nEnter 1 to encrypt. Enter 2 to decrypt: ")
        if encrypt_decrypt == '1':
            affine.encrypt()
            break
        elif encrypt_decrypt == '2':
            affine.decrypt()
            break
        else:
            print("\nTry again! That is not a valid choice!")


def run_atbash_cipher():
    """this method prompts the user if they would like to encrypt or decrypt
    and runs the encrypt or decrypt method of this cipher
    """
    atbash = Atbash()
    while True:
        encrypt_decrypt = input("\nEnter 1 to encrypt. Enter 2 to decrypt: ")
        if encrypt_decrypt == '1':
            atbash.encrypt()
            break
        elif encrypt_decrypt == '2':
            atbash.decrypt()
            break
        else:
            print("\nTry again! That is not a valid choice!")

def run_keyword_cipher():
    """this method prompts the user if they would like to encrypt or decrypt
    and runs the encrypt or decrypt method of this cipher
    """
    keyword = Keyword()
    while True:
        encrypt_decrypt = input("\nEnter 1 to encrypt. Enter 2 to decrypt: ")
        if encrypt_decrypt == '1':
            keyword.encrypt()
            break
        elif encrypt_decrypt == '2':
            keyword.decrypt()
            break
        else:
            print("\nTry again! That is not a valid choice!")


if __name__ == '__main__':
    instructions()
    game()
