age = 18
has_address = False

if age >= 18 and has_address:
    print("enter allowed")
else:
    print("entry denied") 


balance = 500
price = 300
is_user_accounnt_exsists = True

if balance >= price and price > 0 and is_user_accounnt_exsists :
    print("order placed")
else:
    print("order denied")


## Or Operator

login_google = True
login_email = False

if login_google or login_email:
    print("allow user")
else:
    print("user not allowed")

## Not Operator

is_blocked = False

if is_blocked == True:
    print("access granted")

if not is_blocked:
    print("access granted")

completed = False
# if user has not completed print retry

if not completed: #completed = false, not completed = true
    print("retry")

   


