# first_name = input("What is your first name?  ")
# print("Hello,", first_name)
# print(first_name, "is learning Python")

# **** For IF, ELSE and ELIF section ****

first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "Daesy": #colon open the body of our if statement
    print(first_name, "is learning Python")
elif first_name == "Gia":
    print(first_name, "is learning with fellow students in the community! Me too!")
else:
    # this is just in case we have a younger user who can't yet read
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow you're {}! If you are confident with your reading already...".format(age))
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))

