alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_input, shift_number):
    encrypted_text = ""
    for char in text_input:
        shifted_index = alphabet.index(char) + shift_number
        if(shifted_index >= len(alphabet)):
            shifted_index -= len(alphabet) # Shift the index back to beginning if the index is longer than length of alphabet
        encrypted_text += alphabet[shifted_index]
    print(f"The encoded text is {encrypted_text}")
    #TODO-2: Inside the 'encrypt' function, shift_number each letter of the 'text_input' forwards in the alphabet by the shift_number amount and print the encrypted text_input.  
    #e.g. 
    #plain_text = "hello"
    #shift_number = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text_input is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == "encode":
    encrypt(text, shift)