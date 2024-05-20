a = [1, 2, 3, 4, 5]
b = ['apple', 'pear', 'orange', 'banana']

print(a[0], a[1], a[-1])
print(b[1])

print(a[1:4],a[::2])
print(b[::2])

print(a[::-1])
print(b[::-1])





a = [1, 2, 3, 4, 5]
b = ['apple', 'pear', 'orange', 'banana']

a.append(6)
b.append("cherry")
print(a, b)

a.insert(1,7)
b.insert(2, "milk")
print(a, b)
a.remove(7)
b.remove("milk")
print(a, b)
last_elem_1 = a.pop(0)
last_elem_2 = b.pop(0)
print(last_elem_1, last_elem_2)
print(a.index(2), b.index("orange"))
a.extend([5, 5, 5])
b.extend(["cherry", "banana", "banana"])
print(a.count(5), b.count("banana"), b.count("cherry"))

print(a, b)
a.sort(reverse=True)
b.sort()
print(a, b)
a.reverse()
b.reverse()
print(a, b)






a = (1, 2, 3, 4, 5, 5, 4)
print(a[0], a[1], a[2])
print(a[:2], a[-2:])

print(a.count(5), a.count(4))
print(a.index(4))







test_dict = {"user": "Oleg", "age": 21, "county": "Poland"}
print(test_dict["user"], test_dict["age"], test_dict.get("county"))
print(test_dict.get("animal", "key not found"))
test_dict["age"] = 30
print(test_dict["age"])
test_dict ["animal"] = "cat"
print(test_dict["animal"])
animal = test_dict.pop("animal")
print(test_dict)
print(animal)







test_dict = {"user": "Oleg", "age": 21, "county": "Poland"}
copy_test = test_dict.copy()
test_dict.clear()
print(test_dict)
print(copy_test)

for key, value in copy_test.items():
    print(f"Key: {key}, Value: {value}")


wrong_key = copy_test.pop("currency", "key not found")
print(wrong_key)

dict_update = {"new_role": "admin", "salary": 10000}
copy_test.update(dict_update)
print(copy_test)




