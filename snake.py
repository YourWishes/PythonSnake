import os
import time;
import msvcrt
from random import randint

width = 60
height = 22

xv = yv = 0
px = py = 10
ax, ay = 15, 15
trail=[]
tail = 5;
xv = 1
score = 0
hs = 0

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class SnakePart:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

def draw():
    global px, py, xv, yv, ax, ay, trail, tail,score,hs
    
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == "a":
            xv = -1
            yv = 0
        if key == "s":
            xv = 0
            yv = 1
        if key == "d":
            xv = 1
            yv = 0
        if key == "w":
            xv = 0
            yv = -1
    
    px += xv
    py += yv
    if px < 0:
        px = width-1
    if py < 0:
        py = height-1
    if px > width-1:
        px = 0
    if py > height-1:
        py = 0
        
    if px == ax and py == ay:
        tail+=1
        score += 1
        ax = randint(0, width-1)
        ay = randint(0, height-1)
        hs = max(hs,score)
    
    lines=[]
    for y in range(0, height):
        line = [];
        for x in range(0, width):
            if x == ax and y == ay:
                line.append("@")
            elif x == px and y == py:
                line.append("#")
            else:
                snek = False
                for i in trail:
                    if i.x == px and i.y == py:
                        tail = 5
                        score = 0
                    if i.x == x and i.y == y:
                        line.append("#")
                        snek = True
                        break
                if not snek:
                    line.append(" ")
        line.append("\n")
        lines.append("".join(line))
    lines.append("Score: "+`score` + "    Use W A S D to move    Highscore: " + `hs`)
    
    trail.append(SnakePart(px,py))
    while(len(trail) > tail):
        trail.pop(0)
        
    log = "".join(lines);
    print(log);
    
    
    
while(True):
    cls();
    draw();
    time.sleep(.08)#Roughly 1/60th (60FPS)