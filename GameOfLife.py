from graphics import *
from time import sleep
from itertools import product
import cProfile
import re
xcoord = 40
ycoord = 40


def formula(x, y):
     return 2 * (x * xcoord + y) + 1




# checks for the surrounding cells
# I used a formula to find a cell's state from given coordinates
# formula = 2 * (x * 11 + y) + 1
#for example: state of cell (1,0) = 23
def check(D, x, y, log1, log2):
    counter = 0
    global logb
    global logd
    logb = []
    logd = []
    if D[2 * ((x - 1) * xcoord + y) + 1] == "a":  # left
        counter += 1
    if D[2 * ((x + 1) * xcoord + y) + 1] == "a":  # right
        counter += 1
    if D[2 * (x * xcoord + y + 1) + 1] == "a":  # up
        counter += 1
    if D[2 * (x * xcoord + y - 1) + 1] == "a":  # down
        counter += 1
    if D[2 * ((x - 1) * xcoord + y + 1) + 1] == "a":  # left - up
        counter += 1
    if D[2 * ((x - 1) * xcoord + y - 1) + 1] == "a":  # left - down
        counter += 1
    if D[2 * ((x + 1) * xcoord + y + 1) + 1] == "a":  # right - up
        counter += 1
    if D[2 * ((x + 1) * xcoord + y - 1) + 1] == "a":  # right - down
        counter += 1
    if counter < 2 or counter > 3:
        if D[2 * (x * xcoord + y) + 1] == "a":
            logd = [x, y]
            log1.append(logd)
            return 0
    if counter == 2:
        return 1
    if counter == 3:
        if D[2 * (x * xcoord + y) + 1] == "d":
            logb = [x, y]
            log2.append(logb)
            return 2



def main():
    win = GraphWin("Game Of Life", 500, 500)
    win.setCoords(0, 0, xcoord, ycoord)
    c_list = []
    for x in range(xcoord):
        for y in range(ycoord):
            rec = Rectangle(Point(x, y), Point(x + 1, y + 1))
            rec.setFill("grey18")
            rec.setOutline("grey25")
            rec.draw(win)
            state = ["d"] # append "dead" after every cell created to figure out which one is dead-alive
            c_list.append(rec)
            c_list.append(state[0])
    print(c_list)

    def createcell(x, y):
        formula(x, y)
        rec = c_list[formula(x, y) - 1]
        rec.undraw()
        rec.setFill("white")
        rec.setOutline("grey25")
        rec.draw(win)
        c_list[formula(x, y)] = "a"


    # create alive cells. yes, I do not know how to create them with my mouse.

    createcell(1,16)
    createcell(1,17)
    createcell(2,16)
    createcell(2,17)
    createcell(11,15)
    createcell(11,16)#
    createcell(11,17)
    createcell(12,14)
    createcell(12,18)
    createcell(13,19)
    createcell(13,13)
    createcell(14,13)
    createcell(14,19)
    createcell(15,16)#tek nokta
    createcell(17,16)
    createcell(18,16)#uc
    createcell(17,17)
    createcell(16,18)
    createcell(17,15)
    createcell(16,14)
    createcell(23,16)#alt uc
    createcell(22,17)
    createcell(21,17)
    createcell(22,18)
    createcell(21,18)
    createcell(22,19)#sag ust kose dikdortgen
    createcell(21,19)
    createcell(23,20)
    createcell(25,20)
    createcell(25,21)
    createcell(25,16)
    createcell(25,15)
    createcell(35,19)
    createcell(36,19)
    createcell(35,18)
    createcell(36,18)





    sleep(5)
    while True:
        log_dead = []
        log_born = []
        for a, b in product(range(1, xcoord - 1), range(1, ycoord - 1)):
            check(c_list, a, b, log_dead, log_born)
        sleep(0)

        for a in range(len(log_dead)):
            logx = log_dead[a][0]
            logy = log_dead[a][1]
            rec = c_list[2 * (logx * xcoord + logy)]
            rec.undraw()
            sleep(0)
            rec.setFill("grey18")
            rec.setOutline("grey25")
            rec.draw(win)
            c_list[2 * (logx * xcoord + logy) + 1] = "d"
            sleep(0)

        for a in range(len(log_born)):
            logx = log_born[a][0]
            logy = log_born[a][1]
            rec = c_list[2 * (logx * xcoord + logy)]
            rec.undraw()
            sleep(0)
            rec.setFill("white")
            rec.setOutline("grey25")
            rec.draw(win)
            c_list[2 * (logx * xcoord + logy) + 1] = "a"
            sleep(0)



main()
