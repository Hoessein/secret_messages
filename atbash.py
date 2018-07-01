from cipher import Cipher

class Atbash(Cipher):

    #list comprehensions saved in variables to use later.
    alphabet_list = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
    alphabet_list_reversed = [letter for letter in 'zyxwvutsrqponmlkjihgfedcba']

    #dict comprehensions. I can enter the value of the key in one of the dict and the key's value in the other dict.
    atbash_encrypt_dict = {letter: rev_letter for letter, rev_letter in zip(alphabet_list, alphabet_list_reversed)}
    atbash_decrypt_dict = {rev_letter: letter for rev_letter, letter in zip(alphabet_list_reversed, alphabet_list)}


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
            if letter in self.atbash_encrypt_dict:
                output += str(self.atbash_encrypt_dict[letter])
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
            if letter in self.atbash_decrypt_dict:
                output += (str(self.atbash_decrypt_dict[letter]))
            else:
                output += letter
        print("\nHere is your decryption:", output.upper())
