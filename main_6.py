def encoder(x):
    encode_int = ""
    for num in x:
        num=(int(num)+3)%10
        num=str(num)
        encode_int = encode_int+num
    return x
def decode(encode_int):
    original_code = ""
    for num in encode_int:
        num=(int(num)-3)%10
        num=str(num)
        original_code=original_code+num
    return original_code



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
            print("Your password has been encoded and stored!\n")

        if option == 2:
            decoded=decode(encode_int)
            print(decoded)
            print(f"The encoded password is {x}, and the original password is {decoded}.")

        if option == 3:
            break
