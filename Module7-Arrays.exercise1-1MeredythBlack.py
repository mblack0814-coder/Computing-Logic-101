
numbers = []
print("Please enter 20 numbers:")
for i in range(20):
        val = int(input(f"Enter number {i + 1}: "))
        numbers.append(val)
print("Here are your numbers in reverse order:") 
reversed_numbers = numbers[::-1]
for num in reversed_numbers:
        print(num)

