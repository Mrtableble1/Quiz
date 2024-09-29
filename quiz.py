import pgzrun

HEIGHT = 800

WIDTH = 800

TITLE = "Quiz"

all_Q = []
Qs = []
Q_counter = 0
Q_present = 0
timer = 10

smg_box = Rect((1,1),(800,100))
skip_box = Rect((600,350),(180,430))
timer_box = Rect((600,120),(180,200))
Q_box = Rect((50,120),(530,200))
option_box1 = Rect((50,350),(250,200))
option_box2 = Rect((50,580),(250,200))
option_box3 = Rect((325,580),(250,200))
option_box4 = Rect((325,350),(250,200))


def times():
    global timer
    timer -= 1
clock.schedule_interval(times,1)


def draw():
    screen.fill("black")
    screen.draw.filled_rect(smg_box,"blue")
    screen.draw.filled_rect(skip_box,"red")
    screen.draw.filled_rect(timer_box,"purple")
    screen.draw.filled_rect(Q_box,"yellow")
    screen.draw.filled_rect(option_box1,"green")
    screen.draw.filled_rect(option_box2,"green")
    screen.draw.filled_rect(option_box3,"green")
    screen.draw.filled_rect(option_box4,"green")

    screen.draw.textbox("Welcome to the master Quiz!",smg_box)
    screen.draw.textbox("Skip!",skip_box, angle = -90)
    screen.draw.textbox(str(timer),timer_box)
    screen.draw.textbox(Qs[0],Q_box)
    screen.draw.textbox(Qs[1],option_box1)
    screen.draw.textbox(Qs[2],option_box2)
    screen.draw.textbox(Qs[3],option_box3)
    screen.draw.textbox(Qs[4],option_box4)


def option_file():
    global Q_all,Q_counter
    f = open("Q.txt","r")
    Q_all = f.readlines()
    Q_counter = len(Q_all)
    f.close()
option_file()

def read_next_Q():
    global Q_all,Qs
    Qs = Q_all[0].split(",")
read_next_Q()

pgzrun.go()