import turtle
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('level', type=int, nargs='?', default=3)
    parser.add_argument('--size', type=int, default=300)
    parser.add_argument('--speed', type=int, default=0, choices=range(0, 11))
    return parser.parse_args()

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length = length / 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def draw_snowflake(level, size=300, speed=0):
    if level < 0:
        print("invalid level")
        return
    
    screen = turtle.Screen()
    screen.title("Koch Snowflake")
    screen.bgcolor("white")
    screen.setup(width=800, height=800)
    
    t = turtle.Turtle()
    t.speed(speed)
    t.color("blue")
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    
    koch_snowflake(t, size, level)
    t.hideturtle()
    print("done")
    turtle.done()

def main():
    args = parse_arguments()
    draw_snowflake(args.level, args.size, args.speed)

if __name__ == "__main__":
    main()
