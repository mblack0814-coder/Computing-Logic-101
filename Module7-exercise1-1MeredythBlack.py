def main():
    numbers = []

    print("Please enter 20 numbers:")
    for i in range(20):
        val = int(input(f"Enter number {i + 1}: "))
        numbers.append(val)

    print("\nHere are your numbers in reverse order:")
    
    # Python's slice notation [::-1] creates a reversed copy of the list
    reversed_numbers = numbers[::-1]
    
    for num in reversed_numbers:
        print(num)

if __name__ == "__main__":
    main()