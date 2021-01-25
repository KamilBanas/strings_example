name = "kamil banas"

nameInCaps = name.capitalize()
print(nameInCaps)
print(name.capitalize())

print("Count i =", name.count("i"))
print("Count i =", name.count("i",6))

print(name.endswith("as"))
print(name.islower())
print(nameInCaps.islower())

print(name.lstrip("l"))
print(name.replace("s","x"))

#slicing
print(name[0])
print(name[1:4])
print(name[-4])

start = 1
end = 5
print(name[start:end])

email = "kamil.banas@fdmgroup.com"
atIndex = email.index("@")
print(email[0:atIndex])
