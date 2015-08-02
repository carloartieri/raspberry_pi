import curses
import unicornhat as unicorn
from sys import exit
from time import sleep
from random import randint

def get_input(press):
        p = int(stdscr.getyx()[0])+1      #Add 1 to y coordinate for display putposes
        if p > 20:
                p = str(1)
        else:
                p= str(p)
        if press == 258:
                stdscr.addstr('DOWN\t{}\t'.format(p))
                return 'd'        
        if press == 259:
                stdscr.addstr('UP\t{}\t'.format(p))
                return 'u'        
        if press == 260:
                stdscr.addstr('LEFT\t{}\t'.format(p))
                return 'l'        
        if press == 261:
                stdscr.addstr('RIGHT\t{}\t'.format(p))
                return 'r'        
        
        if press == ord('q'):
                curses.endwin()
                exit('Thanks for playing!')

def test_border(pos1,pos2):
        if pos2[0] < 1 or pos2[0] > 6 or pos2[1] < 0 or pos2[1] > 7:
                return pos1
        else:
                return pos2 

def spawn_blue(chance):
        roll = randint(1, 100)
        if roll <= chance:
                return True
        else:
                return False

def update_matrix(matrix, press, time, blue, green=False):
        
        #Scan matrix for elements
        blue_pos = []
        green_pos = []
        db = False
        for x in range(0,8):
                for y in range(0,8):
                        if matrix[x][y][0] == 's':
                                pos1 = [x,y]
                                pos2 = [x,y]
                        if matrix[x][y][0] == 'b':
                                blue_pos.append([x,y])

        #First, move asteroids
        #Blue
        for b in blue_pos:
                if time % 10 == 0:
                        if b[1] + 1 > 7:
                                db = True
                                matrix[b[0]][b[1]] = [None,0,0,0]
                        else:
                                matrix[b[0]][b[1]] = [None,0,0,0]
                                matrix[b[0]][b[1]+1] = ['b',0,0,255]

        #Next spawn new asteroids
        if blue is True:
                spawn_pos = randint(1,7)
                matrix[spawn_pos][0] = ['b',0,0,255]

        #Next move ship
        pressed = False
        if press == 'd':
                pos2[1] += 1
                pressed = True
        elif press == 'u':
                pos2[1] -= 1
                pressed = True
        elif press == 'l':
                pos2[0] -= 1
                pressed = True
        elif press == 'r':
                pos2[0] += 1
                pressed = True

        ship_pos = test_border(pos1,pos2)
        if ship_pos != pos1 and matrix[pos1[0]][pos1[1]][0] == 's':
                matrix[pos1[0]][pos1[1]] = [None,0,0,0]
        if matrix[ship_pos[0]][ship_pos[1]][0] == 'b' or matrix[ship_pos[0]][ship_pos[1]][0] == 'g':
                stdscr.addstr('DIE!!!!!\n')
                stdscr.refresh()
                matrix[ship_pos[0]][ship_pos[1]] = ship
        else:
                matrix[ship_pos[0]][ship_pos[1]] = ship   
        
        if pressed == True:
                stdscr.addstr('{}\tBLUE: {}\n'.format(ship_pos, dodge_blue))
                stdscr.refresh()
        if stdscr.getyx()[0] > 20:
                for i in range(20):
                        stdscr.move(0, 0)
                        stdscr.deleteln()
                stdscr.move(1, 0)
                stdscr.refresh()       
                
        return matrix,db

# def move_ship(pos,press):
#         pos1 = list(pos)
#         pos2 = list(pos)
#         if press == 'd':
#                 pos2[1] += 1
#         elif press == 'u':
#                 pos2[1] -= 1
#         elif press == 'l':
#                 pos2[0] -= 1
#         elif press == 'r':
#                 pos2[0] += 1
#         else:
#                 return test_border(pos1,pos2)
#         strpos = test_border(pos1,pos2)
#         stdscr.addstr('{}\n'.format(strpos))
#         stdscr.refresh()
#         if stdscr.getyx()[0] > 20:
#                 for i in range(20):
#                         stdscr.move(0, 0)
#                         stdscr.deleteln()
#                 stdscr.move(1, 0)
#                 stdscr.refresh()       
#         return test_border(pos1,pos2)

def initialize():
        for i in range(8):
                unicorn.set_pixel(0,i, 255,255,255)
                unicorn.set_pixel(7,i, 255,255,255)        
                unicorn.show()
                sleep(0.1-i*float(0.01))

        ship_pos = [3,7]
        for i in range(2): 
                
                unicorn.set_pixel(ship_pos[0],ship_pos[1], ship[1], ship[2], ship[3])
                unicorn.show()
                sleep(0.2)
                unicorn.set_pixel(ship_pos[0],ship_pos[1], 0,0,0)
                unicorn.show()
                sleep(0.2)
        
        cell = [None,0,0,0] 
        temp_mat = []
        matrix = []
        for y in range(0,8):
                temp_mat.append(list(cell))
        for x in range(0,8):
                matrix.append(list(temp_mat))

        matrix[ship_pos[0]][ship_pos[1]] = ship
        print matrix
        unicorn.set_pixel(ship_pos[0],ship_pos[1], ship[1], ship[2], ship[3])
        unicorn.show()
        return matrix

def lightspeed(lpos,time):
        rails = [255,255,255]
        lcol1 = [255,255,150]
        lcol2 = [255,255,50]
        for i in range(8):
                unicorn.set_pixel(0,i, rails[0],rails[1],rails[2])
                unicorn.set_pixel(7,i, rails[0],rails[1],rails[2])
        unicorn.set_pixel(0,lpos, lcol1[0],lcol1[1],lcol1[2])        
        unicorn.set_pixel(7,lpos, lcol1[0],lcol1[1],lcol1[2])
        if lpos - 1 > -1:
                 unicorn.set_pixel(0,lpos-1, lcol2[0],lcol2[1],lcol2[2])        
                 unicorn.set_pixel(7,lpos-1, lcol2[0],lcol2[1],lcol2[2])
        else:
                 unicorn.set_pixel(0,7, lcol2[0],lcol2[1],lcol2[2])        
                 unicorn.set_pixel(7,7, lcol2[0],lcol2[1],lcol2[2])         
        if time % 2 == 0:
                if lpos + 1 > 7:
                        lpos = 0 
                else:
                        lpos += 1
        return lpos                   

if __name__ == '__main__':

        #Initialize curses
        stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        stdscr.nodelay(1)
        stdscr.keypad(1)

        #Initialize the Unicorn Hat
        unicorn.brightness(0.1)
        unicorn.rotation(180)

        ship = ['s',255,0,0]
        ship_pos = [3,7]
        matrix = initialize()
        
        #Global variables
        time = 0
        lpos = 0        #Position of lightspeed trails
        dodge_blue = 0  #How many blue asteroids dodged
        dodge_green = 0  #How many blue asteroids dodged

        while True:
                press = get_input(stdscr.getch()) #Get input
                #ship_pos = move_ship(ship_pos,press)        
                
                sleep(0.01)
                time += 1
                unicorn.clear()
                matrix,db = update_matrix(matrix,press,time,spawn_blue(5), False)
                if db is True:
                        dodge_blue += 1
                for x in range(0,8):
                        for y in range(0,8):
                                unicorn.set_pixel(x,y, matrix[x][y][1], matrix[x][y][2], matrix[x][y][3])
                lpos = lightspeed(lpos,time)
                unicorn.show() 

                if time == 10000:
                        time = 0
