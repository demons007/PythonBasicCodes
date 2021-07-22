# Python Guess correct number using while: 22-7-2021
# variables:
secret_number = int("3")
low_limit = int("0")
high_limit = int("3")

print("::Guess the correct number in three chance::")

while high_limit > low_limit:
    guess = int(input("Guess the number:"))
    low_limit += 1
    if guess == secret_number:
        print("You won")
        break
else:
    print("Try Again!!!")
