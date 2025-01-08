word = "Donkey"

with open("code-with-harry/chapter-9/donkey.txt") as f:
    context = f.read()

contextNew = context.replace("Donkey", "######")

with open("code-with-harry/chapter-9/donkey.txt", "w") as f:
    f.write(contextNew)