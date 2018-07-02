from cipher import Cipher


class Keyword(Cipher):
    # list comprehensions saved in variables to use later.

    def __init__(self):
        self.encrypted_list = self.keyword_pad()
        self.alphabet_list = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']

    def encrypted_dict(self):
        """dict comprehension so i can enter the dict's value's and key's easily."""
        keyword_encrypt_dict = {letter: keyletter for letter, keyletter in zip(self.alphabet_list, self.encrypted_list)}
        return keyword_encrypt_dict

    def decrypted_dict(self):
        """a simple dict comprehension, love these"""
        keyword_decrypt_dict = {keyletter: letter for keyletter, letter in zip(self.encrypted_list, self.alphabet_list)}
        return keyword_decrypt_dict

    def keyword_pad(self):
        """first i make an empty list and ask the user to enter a keyword
            then i loop through the prompt and place them in a empty variable "holder"
            then i loop through "holder" and check if any value in "holder" is in the alphabet_list
            those items then get removed.
            In the loop I also append each item in "holder" to encrypted_list_copy
            and finally extend encrypted_list_copy to alphabet_list"""

        encrypted_list_copy = []

        keyword = input("\nPlease enter a keyword: ")
        holder = ""

        for a in keyword:
            holder += a

        for x in holder:
            if x in self.alphabet_list:
                self.alphabet_list.remove(x)
                encrypted_list_copy.append(x)

        encrypted_list_copy.extend(self.alphabet_list)

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



