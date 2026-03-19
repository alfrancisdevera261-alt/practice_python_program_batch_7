text = input("Enter a text: ")
modified_character = ""


for characters in text:
    if characters.islower():
        modified_character += characters.swapcase()
    else:
        modified_character += characters
print(modified_character)