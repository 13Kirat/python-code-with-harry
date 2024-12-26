name = "kirat"

length  = len(name)
nameshort  = name[0:3]

print(nameshort)
print(name[-4:-1])
print(name[1:4])
print(name[1:]) # length
print(name[:4]) # zero

word = "amazing"

print(word[1:6:3])

# STRING FUNCTIONS 

print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.title())
print(name.count())
print(name.find("hg")) # return its index
print(name.replace("good","bad"))

# f string functions
print(f"my name is {name}")