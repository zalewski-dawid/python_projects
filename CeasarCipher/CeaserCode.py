#Dawid Zalewski
#Program that allows to encode and decode messages in Ceasar Cipher

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(logo)
def encoding(user_message,shift_number):
    encoded_message = ""
    n=0
    while n<len(user_message):
        equal = 'false'
        for i in range(0,len(alphabet)):

            if alphabet[i]==user_message[n]:
                equal='true'

                if i+shift_number>=len(alphabet):

                    new_index = (i + shift_number) % len(alphabet)
                    encoded_message+=alphabet[new_index]
                else:
                    new_index = i + shift_number
                    encoded_message+=alphabet[new_index]
        if equal=='false':
            encoded_message+= user_message[n]
                #symbols or numbers

        n+=1
    print(f"Here is the encoded message: {encoded_message}")
def decoding(user_message,shift_number):
    decoded_message = ""

    n = 0
    while n < len(user_message):
        equal = 'false'
        for i in range(0, len(alphabet)):

            if alphabet[i] == user_message[n]:
                equal = 'true'

                if i - shift_number < -1*len(alphabet):

                    new_index = (-1*(i - shift_number)) % len(alphabet)


                if i-shift_number<0 and i-shift_number>=-1*len(alphabet):
                    new_index=i-shift_number

                else:
                    new_index = i - shift_number

                decoded_message += alphabet[new_index]
        if equal == 'false':
            decoded_message += user_message[n]
            # symbols or numbers

        n += 1

    print(f"Here is the decoded message: {decoded_message}")


user_choice='true'
while user_choice=='true':

    user_option = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    user_message = input("Type your message: \n").lower()
    shift_number=int(input("Type shift number: \n"))


    if user_option=="encode":
        encoding(user_message,shift_number)

    else:
        decoding(user_message,shift_number)



    choice=input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    if choice=="no":
        user_choice='false'
        print("See ya next time !")


