def encoder(x):
    encode_int = ""
    for num in x:
        num=(int(num)+3)%10
        num=str(num)
        encode_int = encode_int+num
    return x


if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("\nPlease enter an option: "))

        if option == 1:
            x = input("Please enter your password to encode: ")
            encode_int = encoder(x)
            print("Your password has been encoded and stored\n")

        if option == 2:
            x = input("Please enter you")
            print(encode_int)
            #print(f'The encoded password is {encode_int}, and the original password is {x}\n')

        if option == 3:
            break
