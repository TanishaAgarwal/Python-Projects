import turtle as t
import random as rd

t.bgcolor('green')

# snake 
snake = t.Turtle()
snake_shape = ((0,0),(10,0),(10,10),(0,10))
t.register_shape('snake',snake_shape)
snake.shape('snake')
snake.speed(0)
snake.penup()
snake.hideturtle()

# food
food = t.Turtle()
food.shape('circle')
food.color('red') 
food.penup()
food.hideturtle()
food.speed()

# front text
game_started = False
text_turtle = t.Turtle()
text_turtle.write("Press the spacebar-key to start the game", align='center', font=('Arial',20,'bold'))
text_turtle.hideturtle()

# score
score = t.Turtle()
score.hideturtle()
score.speed(0)


def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = snake.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

def place_food():
    food.hideturtle()
    food.setx(rd.randint(-200,200))
    food.sety(rd.randint(-200,200))
    food.showturtle()

def game_over():
    snake.color('green')
    food.color('green')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER !!', align='center', font=('Arial', 30, 'bold'))

def display_score(current_score):
    score.clear()
    score.penup()
    x = (t.window_width() / 2)-30
    y = (t.window_height() / 2)-55
    score.setpos(x,y)
    score.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    current_score = 0
    text_turtle.clear()

    snake_speed = 2
    snake_length = 3
    snake.shapesize(1,snake_length,1)
    snake.showturtle()
    display_score(current_score)
    place_food()

    while True:
        snake.forward(snake_speed)
        if snake.distance(food)<20:
            place_food()
            snake_length = snake_length + 1
            snake.shapesize(1,snake_length,1)
            snake_speed = snake_speed + 1
            current_score = current_score + 10
            display_score(current_score)
        if outside_window():
            game_over()
            break

def move_up():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def move_down():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def move_left():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def move_right():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()