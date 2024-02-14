password = "SE"
password_length = len(password)

# if len(password) <6:
#     strenth = "Weak"
# elif len(password) <=10:
#     strenth = "Medium"
# else:
#     strenth = "Strong"

# print("password strength is", strenth)

if password_length<6:
    strenth = "Weak"
elif password_length <=10:
    strenth = "Medium"
else:
    strenth = "Strong"

print("password strength is", strenth)