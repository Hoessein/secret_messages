from cipher import Cipher


class Keyword(Cipher):

    def __init__(self):
        self.alphabet_list = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
        self.encrypted_list = self.keyword_pad()
        print(len(self.encrypted_list))

    def encrypted_dict(self):
        """dict comprehension so i can enter the dict's value's and key's easily."""
        keyword_encrypt_dict = {letter: keyletter for letter, keyletter in zip(self.alphabet_list, self.encrypted_list)}
        return keyword_encrypt_dict

    def decrypted_dict(self):
        """a simple dict comprehension, love these"""
        keyword_decrypt_dict = {keyletter: letter for keyletter, letter in zip(self.encrypted_list, self.alphabet_list)}
        return keyword_decrypt_dict

    def keyword_pad(self):
        """prompt the user for an input to use as keyword"""

        #An empty list to append the keyword alphabet to
        encrypted_list_copy = []

        #a copy of the instance variable alphabet_list where I can remove letters from
        a_list = self.alphabet_list[:]

        keyword = input("\nPlease enter a keyword: ")
        holder = ""

        for letter in keyword:
            holder += letter

        #in this part i remove each letter from the users input from a_list
        #and also append the input to encrypted_list_copy
        #then extend the remainder of the alphabet list to the encrypted_list_copy
        for letter in holder:
            if letter in a_list:
                a_list.remove(letter)
                encrypted_list_copy.append(letter)

            encrypted_list_copy.extend(a_list)

        return encrypted_list_copy

    def encrypt(self):
        """ prompts user to enter a message
             for loop: to loop through each input
             if statement: checks if the input is in the dict's key,
                 if it is it will append the dict's value to the empty string enc
             finally the print function to print the complete encryption
         """
        output = ""
        message = input("\nEnter your message: ").lower()
        for letter in message:
            if letter in self.encrypted_dict():
                output += str(self.encrypted_dict()[letter])
            else:
                output += letter
        print("\nHere is your encryption:", output.upper())

    def decrypt(self):
        """ prompts user to enter a message
             for loop: to loop through each input
             if statement: checks if the input is in the dict's key,
                 if it is it will append the dict's value to the empty string enc
             finally the print function to print the complete decryption
         """
        output = ""
        message = input("\nEnter your message: ").lower()
        for letter in message:
            if letter in self.decrypted_dict():
                output += str(self.decrypted_dict()[letter])
            else:
                output += letter
        print("\nHere is your decryption:", output.upper())

    def play_again(self):
        for x in self.encrypted_dict():
            del x
        for xx in self.decrypted_dict():
            del xx
