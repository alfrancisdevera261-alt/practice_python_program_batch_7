text = input("Enter a text: ")
suffix = input("Enter the suffix: ")

if text[-len(suffix):] == suffix:
    text_modified = text.replace(suffix, "", 1)
    print(text_modified)
else:
    print("Does not exist")