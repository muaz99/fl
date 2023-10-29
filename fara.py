import turtle

t = turtle.Turtle()
turtle.title("For Fara")

screen=turtle. Screen()
screen.bacolor("black")

# Drawing heart
t.color("red")
t. fillcolor("red")
t.begin_f111()

t. Left(140)
t. forward (180)
t.circle(-90,200)
t. setheading (60) t.circle (-90,280)
t. forward (180)

t.end_$fill()

# Writing text
t.up()
t. setpos (-65, 150) 
t.down() 
t.color( 'lightgreen')
t.vrite("Fara", font=("Verdana", 20, "bold")) 

t.ht()

turtle.mainloopT