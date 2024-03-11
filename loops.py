numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in numbers:
    print(item)

person = {"name": "John", "age": 12, "city": "New York"}

for key, value in person.items():
    print(f"Key: {key} - Value: {value}")

for number in range(5):
    print(number)

for index in range(0, len(person.items())):
    print(index)


cont = 0

while cont < 5:
    print("Cout: ", cont)
    cont += 1
