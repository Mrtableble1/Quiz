import pgzrun

HEIGHT = 800

WIDTH = 800

TITLE = "Quiz"

smg_box = Rect((0,0),(800,100))

def draw():
    screen.fill("black")
    screen.draw.filled_rect(smg_box,"blue")

pgzrun.go()