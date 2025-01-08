words = ["Donkey", "bad", "gande"]

with open("code-with-harry/chapter-9/donkey.txt") as f:
    context = f.read()

for word in words: 
    context = context.replace(word, "#" * len(word))

with open("code-with-harry/chapter-9/donkey.txt", "w") as f:
    f.write(context)