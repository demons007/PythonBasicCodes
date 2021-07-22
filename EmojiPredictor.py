# emoji meaning predictor
def emoji_func(string_value):
    dictionary = {
        ":)": "Happy",
        ":(": "Sad"
    }
    arg1 = dictionary.get(string_value)
    # print(arg1)
    return arg1


x = input(">>")
arg2 = emoji_func(x)
print(f"Meaning is : {arg2}")
