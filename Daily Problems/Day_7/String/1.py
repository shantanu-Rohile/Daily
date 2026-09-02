# 25. Implement Caesar cipher encryption.

def cipher(text, shift):
    old_text = text
    new_text = ""
    for i in old_text:
        if i ==" ":
            new_text += " " 
        else:
            new_text += chr(ord(i)+shift)
    return new_text

text = "somebody is here z"

shift = 1

print(cipher(text,shift))