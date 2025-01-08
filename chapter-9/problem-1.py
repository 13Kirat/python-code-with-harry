f = open("code-with-harry/chapter-9/poem.txt")

content = f.read()
if("twinkle" in content):
    print("the word twinkle is present in content")
else:
    print("the word twinkle is not present in content")

f.close()