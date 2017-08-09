# Ask user for their name
user_name = input("What is your name?: ")

# Ask user for their age
user_age = input("What is your age?: ")

# Ask user where they live
user_location = input("Where do you live?: ")

# Ask user what they enjoy doing
user_enjoyment = input("What do you like to do for fun?: ")

# Create output text
output = "Your name is %s and you are %s years old. You live in %s and you love %s" % (user_name,user_age,user_location,user_enjoyment)

# Print output to screen
print(output)
