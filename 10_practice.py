# PB 1
name = input("Enter your name\nAK")
print("good afternoon, "+ name)

# PB 2
letter = '''Dear <|Name|>,
You are Selected!

Date: <|Date|>
'''

name= input("Enter your name\n")
name= input("Enter Date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", name)
print(letter)

# PB 3
st = "This is a string with double  spaces"
doubleSpaces =st.find("  ")
print(doubleSpaces)

# PB 4
st = "This is a string with double  spaces"
st = st.replace("  "," ")
print(st)

# PB 5
letter ="Dera AK, This Python course is nice! Thanks!"
print(letter)
formatted_letter = "Dear AK,\n\tThis Python course is nice!\nThanks!"
print(formatted_letter)