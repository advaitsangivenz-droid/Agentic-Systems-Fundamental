# Get user name from terminal and print it by converting into upper case
# str.upper() str=name, NAME



# get_name
# make_upper


def get_name():
    name = input("Enter your name: ")
    return name

def make_upper(name):
    return name.upper()


name = get_name()
result = make_upper(name)
print(result)