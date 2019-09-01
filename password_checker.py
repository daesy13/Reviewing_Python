# try password with while only
# then try with only 3 attempts
# when try to exit after the 3 tries need to call SYS
import sys

# to keep the password in one location we have to change it as a constant
MASTER_PASSWORD = "opensesame"
password = input("Please enter the super secret password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, please try again!: ")
    attempt_count += 1
print("Welcome to Secret Town!")