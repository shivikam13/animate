import pgzrun


WIDTH=360
HEIGHT=360

flower=Actor("flower")

def draw():
    screen.clear()
    flower.draw()

animate(flower, pos=(100, 100))




pgzrun.go()