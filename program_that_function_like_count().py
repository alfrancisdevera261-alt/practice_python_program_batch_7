text = input("Enter a text: ")
check_text = input("What are you count text? ")

count_words = 0

for characters in range(len(text)):
    if text[characters:characters+len(check_text)] == check_text:
        count_words += 1
print(count_words)