# Python Guess correct number using while: 22-7-2021
# variables:
secret_name = str("MISTI")

print("::Hey PC who is my Wify :")

while True:
    guess = (input("Enter The Name:")).upper()
    if guess == secret_name:
        print("""
        (ɔ◔‿◔)ɔ♥ -- Yes this is my darling
        """)
        break
    else:
        print("Who the FUK is this")
