# Prompt the user to enter a positive integer
num = int(input("Enter a positive integer: "))

# Check if the number is positive
if num <= 0:
    print("Invalid input!")
else:
    # Print the multiplication table up to 10
    for i in range(1, 13):
        print(num, "x", i, "=", num*i)
