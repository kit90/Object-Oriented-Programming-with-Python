import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('red')

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()
   
def draw_square():
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)

    for _ in xrange(4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

def draw_triangle():
    george = turtle.Turtle()
    george.shape('triangle')
    george.color('green')

    george.left(180)
    
    for _ in xrange(3):
        george.forward(100)
        george.left(120)
        
draw_shapes()
