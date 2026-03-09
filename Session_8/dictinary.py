# name, age, phone

user = {"name": "Alice", "age": 30, "phone": "123-456-7890"}

user2 = {"name": "Bob", "age": 25, "phone": "987-654-3210"}

# key must be unique in a dictionary

row1 = {"col1": "value", "col2": "value2", "col3": "value3"} 

for key, value in user.items():
    print(f"{key}: {value}")

for key, value in user2.items():
    print(f"{key}: {value}")

for key, value in row1.items():
    print(f"{key}: {value}")

