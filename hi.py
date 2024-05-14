print("hello world")
print("Hello world!")
name = "Tom"
Name = "Tom"
print(name, Name)
num_1 = 52
num_2 = 130
num_3 = num_1 - num_2
print(num_3)
num_1 = 53
num = 10
name = 'Tom'

message = 'Tom got some money'
print(name not in message)
name = 'John'
message = 'you won'
print(name in message)

num = 5
print(type(num))
num_2 = 3.14
print(type(3.14))
string  = 'hello'
print(type(string))
check = True
lst = ['hello', 'my', 'name', 'is', 'Tom']
print(type(lst))

tpl = (1, 2, 3)
print(type(tpl))

dct = {'name': 'John', 'age': 25}
print(type(dct))


set_ex = {1, 2, 3, }
print(type(set_ex))

class Person:
    pass

a = Person()
print(type(a))


lst = [1, 2, 3, 4, 5]
dct = {'name': 'Tom', 'age': 5}
name = 'Tom'
tpl = ('n', 'a', 'g')

result = dct['age'] in lst or dct['name'] in tpl
print(result)

print(dct['name'] == name and dct['age'] in lst)

num_1 = '1'
print(type(num_1))



string = 'hello world'
print(len(string))
print(string.upper())
print(string)
string = string.lower()
print(string)
string = string.capitalize()
print(string)
string= string.replace('!', '.')
print(string)
string = string.split()
print(string)
string = string.count('o')
print(string)

print(string)
string = 1
string = str(string)
print(type(string))
base_list = [1, 2, 3]
print(len(base_list))
base_list.append(4)
print(base_list)

base_list.extend([ 5, 6, 7])
print(base_list)

print(base_list.index(4))

base_dict = {'name': 'Tom', 'age': 40, 'high': 180}
print(base_dict.keys())
print(base_dict.values())
print(base_dict.items())

print(base_dict['name'], base_dict.get('is animal', 'No'))







lst = ['Makar', 'is', 'lyabik']
print(type(lst))


tpl = (1, 2, 3, 4, 5, 6)
print(type(tpl))

dct = {'name': 'Egor', 'age': 14, 'high': 167}
print(type(dct))

num = 15
print(type(num))
num_3 = 5.52
print(type(num_3))
string = 'hi-hi'
print(type(string))

class people:
    pass

a = people()
print(type(a))

num_2 = '10'
print(type(num_2))


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dct = {'name': 'Albert', 'age': 40}
tpl = ('o', 'g', 'g')

result = dct['age'] and lst or dct['name'] in tpl
print(result)

print(dct['name'] == name and dct['age'] in lst)

num_str = 125
print(type(num_str))
num_str = '125'
print(type(num_str))

message = 'Hi, my name is Python!'
print(message)
message = message.replace('y', 'o')
print(message)

split_test = 'This is a split test'
print(split_test)
split_test = split_test.split()
print(split_test)



num_5 = 'string_join'
print(len(num_5))


list_append = [1, 2, 3]
print(len(list_append))
print(list_append)
list_append.append(4)
print(list_append)



list_extend = [4, 5, 6]
print(list_extend)
list_extend.extend([7, 8, 9])
print(list_extend.index(6))

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test)
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())






string = 'Hello world!'

if "Hello" in string:
    print("Hello in string")
elif "world" in string:
    print("world in string")


a = 10
b = 20

if a >= 10 and b == 20:
    print(a + b)

    test_list = ["hello", "test", 1, 2, 3]

    if "hello" in test_list and 1 in test_list:
        print("hello 1")
    elif "test" in test_list and 4 not in test_list:
        print("test 4")
    else:
        print("your conditions were whong")







user_1 = {
    'name': 'Tom',
    'age': 21,
    "balance": 20000,
    "carrency": "USD",
    "status": True
}

user_2 = {
    'name': 'John',
    'age': 17,
    "balance": 5000,
    "carrency": "EUR",
    "status": False
}

user_3 = {

    'age': 30,
    "balance": 100000,
    "carrency": "UAH",
    "status": True
}

list_of_carrency = ["USD", "GBR", "UAH", "EUR"]

if user_3.get("name", None) and user_3["age"] >= 18 and user_3["status"]:
    if user_3["balance"] >= 10000 and user_3["carrency"] in list_of_carrency:
        print(f"Hello! You can create your binance account, welkom {user_3['name']}")
    elif user_3["balace"] >= 1000 and user_3["carrency"] in list_of_carrency:
        print("You need more money!")
    else:
        print("Money critical not ehough")
elif not user_3.get(name, None):
    print("Please, write your name in your account discription")
elif user_3["age"] <= 18:
    print("For registry binance account you have to be 18 year old")
else:
    print("Something went wrong")





test_list = ["hello", "test", 1, 2, 3, 4, 5, 6]

for num in test_list:
    print(f"You got a {num} -----<")




test_list = [1, 2, 3, 4, 5]

while len(test_list) < 10:
    test_list.append(3)
    print(test_list)


test_list = ["test", "puthon", "code"]

for s in test_list:
    if s == "test":
        print(s)
    elif s == "python":
        print(s)
    else:
        print(s)





a = 0
add_list = []

while len(add_list) < 100:
    print("len of list: ", len(add_list))
    add_list.append(a)
    a += 1
    if len(add_list) == 50:
        print("You are at middle of list")






user_1 = {
    "user_name": "tester",
    "role": "admin",
    "account_connection": True
}


user_2 = {
    "user_name": "junior",
    "role": "user",
    "account_connection": False
}


user_3 = {
    "user_name": "middle",
    "role": "pro_user",
    "account_connection": True
}

list_of_users = [user_1, user_2, user_3]

for user in list_of_users:
    print(f"Work with {user['user_name']} account -----<<<<")
    if not user["account_connection"]:
        count_of_tries = 10
        while count_of_tries != 0:
            if count_of_tries == 5:
                user["account_connection"] = True
            print("Try to connect to user account")
            count_of_tries -= 1
            print("Count of tries left: ", count_of_tries)
    elif user["role"] == "admin":
        print(f"Hello in system {user['user_name']}")
    else:
        print("Welcome on the board")
