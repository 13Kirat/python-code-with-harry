friends = ["Apple", "Orange", 5, 54.54, False]

print(friends[0])
friends[0] = "Grapes"

print(friends[0])

friends.append("Harry")

print(friends[0:4])

print(friends[0:4:2])

print(friends[::2])

print(friends[::-1])

print(friends[-1])

print(friends[-3:-1])

print(len(friends))

print(friends.index("Harry"))

print(friends.count("Apple"))

friends.sort()

friends.reverse()

friends2 = friends.copy()

friends.clear()

print(friends2 + friends)

print(friends2 * 2)

print(friends2.pop())

print(friends2.remove("Apple"))

print(friends2.insert(5, "Apple"))