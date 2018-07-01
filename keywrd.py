from cipher import Cipher

class Keyword(Cipher):

    #list comprehensions saved in variables to use later.
    alphabet_list = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
    encrypted_list = [keyletter for keyletter in 'kryptosabcdefghijlmnquvwxz']

    #dict comprehensions. I can enter the value of the key in one of the dict and the key's value in the other dict.
    keyword_encrypt_dict = {letter: keyletter for letter, keyletter in zip(alphabet_list, encrypted_list)}
    keyword_decrypt_dict = {keyletter: letter for keyletter, letter in zip(encrypted_list, alphabet_list)}

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
            if letter in self.keyword_encrypt_dict:
                output += str(self.keyword_encrypt_dict[letter])
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
            if letter in self.keyword_decrypt_dict:
                output += str(self.keyword_decrypt_dict[letter])
            else:
                output += letter
        print("\nHere is your decryption:", output.upper())
