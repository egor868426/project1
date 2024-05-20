def say_hello(username, age):
    print(f"Hello {username}, welkome to the club, Buddy!")
    print(f"Your age is {age}, you are so butifuly!")
    print("------------------------------------")


def print_numbers(start, stop):
    for num in range(start, stop):
        print(f"Current number is: {num}")

        print("-------------------------")

user_data = {"Dima": 25, "Sara": 34, "Tom": 11}
list_of_ranges = [(1, 10), (2, 9), (0, 100)]

# for name, age in user_data.items():
 #   say_hello(name, age)

for start_pos, stop_pos in list_of_ranges:
    print_numbers(start_pos, stop_pos)















import turtle


def draw_square(size, color):
    turtle.speed(1)
    turtle.color(color)
    turtle.begin_fill()
    def move(len):
        turtle.forward(len)
        turtle.left(90)

    for _ in range(4):
        move(size)

turtle.end_fill()

draw_square(110, 'yellow')
turtle.goto(200 ,200)
draw_square(200, 'blue')









                
