def printTable(num):
    print("Multiplication Table for", {num})
    for i in range(1, 6):
        print("{num} x {i} = {num * i}")

for number in range(2,9):
    printTable(number)



    #sum from 1 to 100
    total=0
    #how many steps:100 steps 0(n)
    for num in range(1,101):
        total += num

    print("total of sum is:", total)

    n=100
    #n*(n+1)--> 0(1)