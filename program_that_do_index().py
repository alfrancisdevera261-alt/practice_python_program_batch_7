text = input("Enter a text: ")
substring = input("Enter the substring: ")

index_count = 0

for characters in range(len(text)):
    if text[characters:characters+len(substring)] != substring:
        index_count += 1
    else:
        print(index_count)
        break