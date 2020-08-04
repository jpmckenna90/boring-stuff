def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        number = number // 2
        if number != 1:
            collatz(number)
    elif number % 2 == 1:
        print(3 * number + 1)
        number = 3 * number + 1
        if number != 1:
            collatz(number)

print("Please enter a number.")
number = int(input())

if number != 1:
    collatz(number)

# this is kinda sloppy and can most certainly be cleaned up
