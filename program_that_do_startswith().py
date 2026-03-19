text = input("Enter a text: ")
preffix = input("Enter the preffix: ")

if text[:len(preffix)] == preffix:
    print(True)
else:
    print(False)