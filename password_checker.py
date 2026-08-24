# Password Strength Analyzer - Week 01
# ITIA 1510 - Cybersecurity Automation

# Collect information about the account and password.
account = input("Enter the account or system: ")

# Username is collected now because it will be used for checks in Week 02.
username = input("Enter the username: ")

# Collect the password that will be analyzed.
password = input("Enter the password: ")

# Collect the rotation interval as a string, then convert it to an integer.
rotation_interval = int(input("Enter password rotation interval in months: "))

# Calculate the password length.
password_length = len(password)

# Calculate a raw numeric strength indicator based on password length.
length_score = password_length * 10

# Calculate how many times the password will be rotated over 3 years.
rotation_count = 36 // rotation_interval

# Display the formatted password analysis report.
print("========================================")
print("       PASSWORD STRENGTH ANALYZER")
print("========================================")
print("Account           :", account)
print("Username          :", username)
print("Password Length   :", password_length)
print("Length Score      :", length_score)
print("Rotation Interval :", rotation_interval, "months")
print("Rotation Count    :", rotation_count)
print("----------------------------------------")
print("NOTE: Classification requires conditionals -- coming in Week 02.")
print("========================================")
