text = input("Enter a text: ")
substring = input("Enter the substring: ")

index_count = 0

for characters in range(len(text) -1, -1, -1):
    if text[characters:characters+len(substring)] != substring:
        index_count = (len(text)-1) - 1
    else:
        print(index_count)
        break
print(len(text))