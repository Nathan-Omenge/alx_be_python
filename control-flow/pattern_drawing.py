#Prompting the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initializing row counter
row = 0

# Using while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line
    row += 1