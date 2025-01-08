f = open("code-with-harry/chapter-9/file.txt")
print(f.read())
f.close()

# using with statement 

with open("code-with-harry/chapter-9/file.txt") as f:
    print(f.read())