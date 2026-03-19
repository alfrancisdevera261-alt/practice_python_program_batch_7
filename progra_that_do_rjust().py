text = input("ENter a text: ")
width = int(input("Enter the desired width: "))

total_width = width - len(text)

if total_width > 0:
    modified_text = " " * total_width + text
else:
    modified_text = text
print(modified_text)
