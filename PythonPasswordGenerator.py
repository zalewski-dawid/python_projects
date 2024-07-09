import random
print("Welcome to the Python Password Generator")
print("IMPOSSIBLE TO CRACK BY HACKERS ;)")
password=""
password_list = []
bool='false'

letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols=["!","@","#","$","%","^","&","*","(",")"]
numbers=["1","2","3","4","5","6","7","8","9"]
while(bool=='false'):
    print("ENTER: 1 (random length and elements)  ENTER: 2 (you declare length of password and amount of specific elements(numbers,letters,symbols))")
    option=int(input("Choose the option of generating the password: "))

    if option==1:
        bool='true'
        random_length_of_password=random.randint(4,16)
        print(f"Generated password length:{random_length_of_password} ")
        nbr_letters = random.randint(1, random_length_of_password - 2)
        nbr_numbers = random.randint(1, random_length_of_password - nbr_letters - 1)
        nbr_symbols = random_length_of_password- nbr_letters - nbr_numbers


        for n in range(1,nbr_symbols+1):
            password_list.append(random.choice(symbols))

        for n in range(1,nbr_numbers+1):
            password_list.append(random.choice(numbers))
        for n in range(1,nbr_letters+1):
            password_list.append(random.choice(letters))


        random.shuffle(password_list)

        for item in password_list:
            password += item

        print(f"YOUR STRONG PASSWORD: {password}")



    elif option==2:
        bool='true'
        bool2='false'
        while(bool2=='false'):
            length_of_password = int(input("Enter the length of password: "))
            nbr_symbols = int(input("How many symbols would you like to generate?: "))
            nbr_letters = int(input("How many letters would you like to generate?: "))
            nbr_numbers = int(input("How many numbers would you like to generate?: "))

            if nbr_letters+nbr_numbers+nbr_symbols == length_of_password:
                bool2='true'
            else:
                print("ERROR: SUM OF SPECIFIC ELEMENTS DO NOT EQUAL DECLARED LENGTH OF PASSWORD")

        for n in range(1,nbr_symbols+1):
            password_list.append(random.choice(symbols))

        for n in range(1,nbr_numbers+1):
            password_list.append(random.choice(numbers))
        for n in range(1,nbr_letters+1):
            password_list.append(random.choice(letters))


        random.shuffle(password_list)

        for item in password_list:
            password += item

        print(f"YOUR STRONG PASSWORD: {password}")
    elif option!=1 and option!=2:
        print("ERROR: WRONG OPTION! ")