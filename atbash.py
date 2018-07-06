from cipher import Cipher


class Atbash(Cipher):

    def __init__(self):
        self.alphabet_list = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
        self.alphabet_list_reversed = [letter for letter in 'zyxwvutsrqponmlkjihgfedcba']

    def encrypted_dict(self):
        """dict comprehension so i can enter the dict's value's and key's easily."""
        atbash_encrypt_dict = {letter: number for letter, number in zip(self.alphabet_list, self.alphabet_list_reversed)}
        return atbash_encrypt_dict

    def decrypted_dict(self):
        """a simple dict comprehension, love these"""
        atbash_decrypt_dict = {number: letter for number, letter in zip(self.alphabet_list_reversed, self.alphabet_list)}
        return atbash_decrypt_dict

    def encrypt(self):
        """ prompts user to enter a message to encrypt
        """
        output = ""
        message = input("\nEnter your message: ").lower()
        for letter in message:
            #if statement: checks if the input is in the dict's key,
            #if it is it will append the dict's value to the empty string enc
            if letter in self.encrypted_dict():
                output += str(self.encrypted_dict()[letter])
            else:
                output += letter
        print("\nHere is your encryption:", output.upper())

    def decrypt(self):
        """ prompts user to enter a message to decrypt
        """
        output = ""
        message = input("\nEnter your message: ").lower()
        for letter in message:
            #if statement: checks if the input is in the dict's key,
            #if it is it will append the dict's value to the empty string enc
            if letter in self.encrypted_dict():
                output += (str(self.encrypted_dict()[letter]))
            else:
                output += letter
        print("\nHere is your decryption:", output.upper())
