# Sabrina Joseph

def encoder(pw):
    encoded_pw = ''
    for num in pw:
        encoded_digit = str(int(num) + 3)  # Shifting each digit up by 3
        encoded_pw += encoded_digit
    return encoded_pw

#Decode function
def decode(password):
    decoded_pw = ""
    for i in password:
        decode_new = int(i) - 3
        decoded_pw += str(decode_new)

    return decoded_pw


def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

def main():
    while True:
        menu()
        try:
            option = int(input("Please enter an option: "))
            if option == 1:
                password = input("Please enter your password to encode: ")
                encoded_password = encoder(password)
                print("Your password has been encoded and stored!\n")
            elif option == 2:
                print(f"The encoded password is {encoder(password)}, and the original password is {decode(encoder(password))}.\n")

            elif option == 3:
                exit()
        except ValueError:
            print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()