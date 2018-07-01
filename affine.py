from cipher import Cipher


class Affine(Cipher):

    #list comprehensions saved in variables to use later.
    alphabet_list = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
    numbers_list = [number for number in range(0,27)]

    #dict comprehensions. I can enter the value of the key in one of the dict and the key's value in the other dict.
    affine_encrypt_dict = {letter: number for letter, number in zip(alphabet_list, numbers_list)}
    affine_decrypt_dict = {number: letter for number, letter in zip(numbers_list, alphabet_list)}


    enc_list = []

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
            if letter in self.affine_encrypt_dict:
                output += str(self.affine_encrypt_dict[letter])
                output += ","
            else:
                output += letter

        print("\nHere is your encryption:", output[:-1])

    def decrypt(self):
        """ prompts user to enter a message
             for loop: to loop through each input
             if statement: checks if the input is in the dict's key,
                 if it is it will append the dict's value to the empty string enc
             the user is asked to comma separate their input
             otherwise there's no way to distinguish double digit numbers
             a try is used to catch the program from breaking if the user inputs something other than an int.
            finally the print function to print the complete decryption
         """
        print("\nPlease comma separate the message you would like to decrypt")
        while True:
            output = ""
            message = input("\nEnter your message: ").lower()
            new_message = message.split(",")
            try:
                for number in new_message:
                    if int(number) in self.affine_decrypt_dict:
                        output += self.affine_decrypt_dict[int(number)]
            except ValueError:
                print("\nYour input can't be decrypted completely. "
                      "Please comma separate the input and add numbers only. ")
            else:
                print("\nHere's your decryption:", output.upper())
                break
