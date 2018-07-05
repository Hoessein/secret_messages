from cipher import Cipher


class Affine(Cipher):

    def __init__(self):
        self.alphabet_list = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
        self.numbers_list = [number for number in range(0, 27)]

    def encrypted_dict(self):
        """dict comprehension so i can enter the dict's value's and key's easily."""
        affine_encrypt_dict = {letter: number for letter, number in zip(self.alphabet_list, self.numbers_list)}
        return affine_encrypt_dict

    def decrypted_dict(self):
        """a simple dict comprehension, love these"""
        affine_decrypt_dict = {number: letter for number, letter in zip(self.numbers_list, self.alphabet_list)}
        return affine_decrypt_dict

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
                output += ","
            else:
                output += letter

        print("\nHere is your encryption:", output[:-1])

    def decrypt(self):
        """ prompts user to enter a message and handels the decryption
         """
        print("\nPlease comma separate the message you would like to decrypt")
        while True:
            output = ""
            message = input("\nEnter your message: ").lower()
            new_message = message.split(",")
            # a try is used to catch the program from breaking if the user inputs something other than an int.
            try:
                for number in new_message:
                    #if statement: checks if the input is in the dict's key,
                    #if it is it will append the dict's value to the empty string enc
                    if int(number) in self.decrypted_dict():
                        output += self.decrypted_dict()[int(number)]
            except ValueError:
                #the user is asked to comma separate their input
                # otherwise there's no way to distinguish double digit numbers

                print("\nYour input can't be decrypted completely. "
                      "Please comma separate the input and add numbers only. ")
            else:
                print("\nHere's your decryption:", output.upper())
                break
