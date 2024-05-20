a = [1, 2, 3, 4, 5, 6, 7]
print(a[0], a[2], a[-1])

print(a[:2], a[::4])

a.insert(9, 10)
a.insert(10, 20)
print(a)
a.remove(10)
print(a)




a = [1, 2, 3, 4, 5]
test_list = [1 + 2 + 3 + 4 + 5]
print(test_list)





a = (13, 29, 11, 4, 60)
multiplied_a = [a * 2 for a in a]
print(multiplied_a)




fruits = ("apple", "banana", "orange")
print(fruits[0])
print(fruits[1])
print(fruits[2])




num_1 = (1, 2, 3)
num_2 = (4, 5, 6)
print(num_1 + num_2)





my_fav = {"name": "Cristiano.Ronaldo", "age": 39, "sport": "Football", "team": "Al-Nasr"}
print(my_fav["name"], my_fav["age"], my_fav["sport"], my_fav["team"])
print(my_fav.get("book", "key not found"))
my_fav ["book"] = "Harry-Potter"
print(my_fav["book"])
book = my_fav.pop("book")
print(my_fav)
print(book)





countries_and_capitals = {"Ukraine": "Kiiv", "France": "Paris", "Gegmany": "Berlin", "Japan": "Tokyo"}
print(countries_and_capitals)
counry = input("Enter a country name: ")
if county in countries_and_capitals:
    print(f"capital {country}: {countries_and_capitals[country]}")
else:
    print("country not found")



