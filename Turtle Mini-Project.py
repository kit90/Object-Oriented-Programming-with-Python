import turtle, math

window = turtle.Screen()

brad = turtle.Turtle()
brad.shape('turtle')
brad.color('blue')

brad.rt(90)
brad.fd(200)
brad.lt(90)

brad.pu()
brad.fd(100)
brad.lt(135)
brad.pd()

brad.fd(100 * math.sqrt(2))
brad.rt(90)
brad.fd(100 * math.sqrt(2))
brad.rt(45)

brad.pu()
brad.fd(150)
brad.rt(180)
brad.pd()

brad.fd(100)
brad.lt(90)
brad.fd(200)
brad.lt(90)
brad.fd(100)

window.exitonclick()

