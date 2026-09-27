student = {
    "name": "Ranjay",
    "age": 20,
    "course": "Python"
}

key = input("Enter a key: ")

try:
    print("Value:", student[key])

except KeyError:
    print("Key not found.")