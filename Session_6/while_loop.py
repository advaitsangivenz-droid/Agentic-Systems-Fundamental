count = 0


while count < 3:      #while the condition is true keep looping
    print(count)
    print("hello")
    count = count + 1


# You ask user to enter password till he/she doesn't enter the correct password

actual_password = "today"

password = ""
while password != actual_password:
    password = input("Enter your password:")

    