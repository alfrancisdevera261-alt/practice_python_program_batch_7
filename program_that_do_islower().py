text = input("Enter a text: ")
is_all_lower = True

for characters in text:
    if characters.isupper:
        is_all_lower = False
    else:
        is_all_lower = True
print(is_all_lower)