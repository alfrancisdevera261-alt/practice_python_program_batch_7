text = input("Enter a text: ")
spaces = ""
for characters in reversed(text):
    if characters == " ":
        spaces += " "
    else:
        break
result = text.removesuffix(spaces)
print(result)