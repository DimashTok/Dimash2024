import pygame
pygame.init()

#basic settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

#color names
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
color = colorRED

clock = pygame.time.Clock()

#figures are False for def
circle = False
rec = False
lastik = False
square = False
right_triangle = False
Romb = False
equilateral_triangle = False

#additional settings
LMBpressed = False
THICKNESS = 5
done = False

#basic coordinates 
currX = 0
currY = 0
prevX = 0
prevY = 0

#function for rectangle
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

#function for square
def calculate_square(x1, y1, x2, y2): 
    if x2<x1 and y2>y1:
        x0, y0 = x1, y1
        x3, y3 = x2, y2 
        lx, ly = abs(x3-x0), abs(y3-y0)
        l = max(lx, ly)
        x4, y4 = abs(x0-l), y0
        x5, y5 = x0, abs(y0+l)
        return [(x0,y0),(x5,y5),(x4,y5),(x4,y4)]
    elif x2>x1 and y2<y1:
        x0, y0 = x1, y1
        x3, y3 = x2, y2
        lx, ly = abs(x3-x0), abs(y3-y0)
        l = max(lx, ly)
        x4, y4 = abs(x0+l), y0
        x5, y5 = x0, abs(y0-l)
        return [(x0,y0),(x4,y4),(x4,y5),(x5,y5)]
    elif x2<x1 and y2<y1:
        x0, y0 = x1, y1
        x3, y3 = x2, y2 
        lx, ly = abs(x3-x0), abs(y3-y0)
        l = max(lx, ly)
        x4, y4 = abs(x0-l), y0
        x5, y5 = x0, abs(y0-l)
        return [(x0,y0),(x4,y4),(x4,y5),(x5,y5)]
    else:
        x0, y0 = min(x1, x2), min(y1, y2)
        x3, y3 = max(x1, x2), max(y1, y2)
        lx, ly = abs(x3-x0), abs(y3-y0)
        l = max(lx, ly)
        x4, y4 = x0 + l, y0
        x5, y5 = x0, y0 + l
        return [(x0,y0),(x4,y4),(x4,y5),(x5,y5)]    

#function for circle
def calculate_circle(x1, y1, x2, y2):
    center_x = min(x1, x2) + abs(x1 - x2) // 2
    center_y = min(y1, y2) + abs(y1 - y2) // 2
    radius = min(abs(x1 - x2), abs(y1 - y2)) // 2
    return (center_x, center_y), radius

#function for right triangle
def calculate_right_triangle(x1, y1, x2, y2):
    x0, y0 = min(x1, x2), min(y1, y2)
    x3, y3 = max(x1, x2), max(y1, y2)
    x4 = x0
    y4 = y3
    return [(x0,y0),(x4,y4),(x3,y3)]

#function for romb
def calculate_romb(x1, y1, x2, y2):
    x0, y0 = min(x1, x2), min(y1, y2)
    x3, y3 = max(x1, x2), max(y1, y2)
    x4, y4 = x0 + (abs(x3 - x0))/2, y0
    x5, y5 = x4, y3
    x6, y6 = x0, y0 + (abs(y3 - y0))/2
    x7, y7 = x3 , y6
    return [(x4, y4),(x6, y6),(x5, y5),(x7, y7)]

#function for equilateral triangle
def calculate_equilateral_triangle(x1, y1, x2, y2):
    x0, y0 = min(x1, x2), min(y1, y2)
    x3, y3 = max(x1, x2), max(y1, y2)
    x4, y4 = x0 + (abs(x3 - x0))/2, y0
    x5, y5 = x0, y3
    return [(x4,y4),(x5,y5),(x3,y3)]


while not done:
    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))

        #escape buttons
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True  

        #HICKNESS buttons
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1  

        #color buttons
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            color = colorRED
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            color = colorBLUE
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            color = colorWHITE
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            color = colorGREEN

        #shapes buttons
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            rec = True
            circle = False
            lastik = False
            square = False
            right_triangle = False
            Romb = False
            equilateral_triangle = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            circle = True
            rec = False
            lastik = False
            square = False
            right_triangle = False
            Romb = False
            equilateral_triangle = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            lastik = True
            rec = False
            circle = False
            square = False
            right_triangle = False
            Romb = False
            equilateral_triangle = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            square = True
            circle = False  
            rec = False  
            lastik = False
            right_triangle = False
            Romb = False
            equilateral_triangle = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            square = False
            circle = False  
            rec = False  
            lastik = False
            right_triangle = True
            Romb = False
            equilateral_triangle = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            square = False
            circle = False  
            rec = False  
            lastik = False
            right_triangle = False
            Romb = True
            equilateral_triangle = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            square = False
            circle = False  
            rec = False  
            lastik = False
            right_triangle = False
            Romb = False
            equilateral_triangle = True

        #drawing eraser with mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            if lastik:
                pygame.draw.rect(screen, colorBLACK, (event.pos[0], event.pos[1], 15, 15))
        
        #drawing other shapes with mouse
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if rec:
                    pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                if circle:
                    center, radius = calculate_circle(prevX, prevY, currX, currY)
                    pygame.draw.circle(screen, color, center, radius, THICKNESS)  
                if square:
                    pygame.draw.polygon(screen, color,calculate_square(prevX, prevY, currX, currY), THICKNESS)
                if right_triangle:
                    pygame.draw.polygon(screen, color,calculate_right_triangle(prevX, prevY, currX, currY), THICKNESS)
                if Romb:
                    pygame.draw.polygon(screen, color,calculate_romb(prevX, prevY, currX, currY), THICKNESS)
                if equilateral_triangle:
                    pygame.draw.polygon(screen, color,calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
                
        #drawing eraser
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]  
                if lastik:
                    pygame.draw.rect(screen, colorBLACK, (event.pos[0], event.pos[1], 15, 15))          
                    base_layer.blit(screen, (0, 0))

        #drawing other shapes               
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if rec:
                pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            if circle:
                center, radius = calculate_circle(prevX, prevY, currX, currY)
                pygame.draw.circle(screen, color, center, radius, THICKNESS)   
            if lastik:
                pygame.draw.rect(screen, colorBLACK, (event.pos[0], event.pos[1], 15, 15))    
            if square:
                pygame.draw.polygon(screen, color,calculate_square(prevX, prevY, currX, currY), THICKNESS)
            if right_triangle:
                pygame.draw.polygon(screen, color,calculate_right_triangle(prevX, prevY, currX, currY), THICKNESS)
            if Romb:
                pygame.draw.polygon(screen, color,calculate_romb(prevX, prevY, currX, currY), THICKNESS)
            if equilateral_triangle:
                pygame.draw.polygon(screen, color,calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
            
            base_layer.blit(screen, (0, 0))
            

    pygame.display.flip()
    clock.tick(60)
    