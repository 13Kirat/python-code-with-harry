f = open("code-with-harry/chapter-9/file.txt")

# lines = f.readlines()
# print(lines)

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# print(line1)
# print(line2)
# print(line3)
# print(line4)

line = f.readline()
while(line!= ""):
    print(line)
    line = f.readline()

f.close()
