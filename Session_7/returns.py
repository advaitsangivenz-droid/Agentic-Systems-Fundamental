def add (a,b):
    sum = a + b
    return (sum)

def subtract (a,b):
    diff = a - b
    print(diff)

sum = add(2,3)
diff = subtract( sum, 1)


def check_access(is_verified):
    if not is_verified:
        return "Access Denied"
    else:
        print("Above 18")
        print("Eligible")
    return "Access Granted"

access = check_access(False)
print(access)
    




#python allows returning  multiple values

def greeting(name):
    greeting_sentence = "hello" + name
    return name, greeting_sentence

name, greeting_sentence = greeting("Advait")
print(name)
print(greeting_sentence)





def sum_and_average(range_value):
    sum = 0
    for i in range(range_value):
        sum = i
    average = sum / range_value
    return sum, average

sum, average = sum_and_average(10)
print(sum)
print(average)    
