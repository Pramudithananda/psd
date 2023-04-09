numbers = [45, 93, 34, 71, 89, 56]

# Initialize variables
total = 0
minimum = numbers[0]
maximum = numbers[0]

# Loop through the list
for num in numbers:
    # Add the number to the total
    total += num
    
    # Check if the number is greater than the current maximum
    if num > maximum:
        maximum = num
    
    # Check if the number is less than the current minimum
    if num < minimum:
        minimum = num

# Calculate the average
average = total / len(numbers)

# Print the results
print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
