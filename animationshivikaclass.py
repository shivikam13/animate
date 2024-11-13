import pgzrun
WIDTH=500
HEIGHT=500
TITLE="Animation Practice"

char=Actor('shrek')
char.pos=50,HEIGHT//5
def start_animation():
    animate(char, pos=(WIDTH - 50, HEIGHT // 2),tween="bounce_start_end", duration=5)
    

def draw():
    screen.clear()
    screen.fill("blue")
    char.draw()
beep = tone.create('A3', 0.5)

def on_mouse_down():
    beep.play()
start_animation()

pgzrun.go()
