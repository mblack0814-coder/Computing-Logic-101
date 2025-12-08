user_input = 0
numbers = []
print("Enter numbers between 1 and 20. Enter -1 to stop.")
while user_input != -1:
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)
print("Here they are in reverse order:")
for i in range(len(numbers) - 1, -1, -1):
        print(numbers[i])


