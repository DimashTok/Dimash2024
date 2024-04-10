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

#function for circle
def calculate_circle(x1, y1, x2, y2):
    center_x = min(x1, x2) + abs(x1 - x2) // 2
    center_y = min(y1, y2) + abs(y1 - y2) // 2
    radius = min(abs(x1 - x2), abs(y1 - y2)) // 2
    return (center_x, center_y), radius

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            circle = True
            rec = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            lastik = True
            rec = False
            circle = False

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
            base_layer.blit(screen, (0, 0))

    pygame.display.flip()
    clock.tick(60)