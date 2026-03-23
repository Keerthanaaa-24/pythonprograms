def palindrome(txt):
    txt = txt.lower().replace("","")
    return txt == txt[::-1]

word = input("Enter a Word/Sentence:")

if palindrome(word):
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")