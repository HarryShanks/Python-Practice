# Create a student email creator that uses first and lat name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables
print ("Welcome to the Student Email Creator for Western Springs College")
first_name = input ("What is your first name?").lower().strip()
last_name = input ("what is your last name?").lower().strip()
student_id = input ("What is your student ID? (List of three digit numbers)").lower().strip()

# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)




# Output the final email address
print ("Your email is " + first_name + last_name + student_id + "@Western_Springs_College.school.nz ")

# Create a temporary password to output as well
print ("Your password is " + first_name.upper() + last_name.upper() +str(float (student_id)/10))
# It should be their names in all uppercase and their id divided by 10