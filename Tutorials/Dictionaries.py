#########################################
# Dictionaries
#########################################

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

phonebook["Jake"] = 938273443
print(phonebook)

phonebook.pop("John")
print(phonebook)
