import turtle

# -------- Écran --------

ecran = turtle.Screen()
ecran.setup(800, 600)
ecran.title("Ciel Bleu")
ecran.bgcolor("light sky blue")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# -------- Fonction étoile --------

def etoile(taille, couleur):
    t.color(couleur)
    t.begin_fill()
    for _ in range(5):
        t.forward(taille)
        t.right(144)
    t.end_fill()

# -------- Une seule grande étoile blanche --------

t.penup()
t.goto(-60, -50)
t.pendown()

etoile(150, "white")

turtle.done()