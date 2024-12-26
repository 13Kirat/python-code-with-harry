d = {}
marks= {
    "Harry": 98,
    "Rohan": 87,
    "Hammad": 75
}

print(marks["Harry"])

print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"Harry" : 99, "renuka": 100}))
print(marks.get("Hammad")) # this will give none
print(marks["Harry2"]) # This will give error
