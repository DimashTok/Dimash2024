import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False

white = (255, 255, 255)
yellow = (255, 255, 0)

font = pygame.font.SysFont("comicsansms", 30)

y = 55

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] :
            y += 60
            if y>480:
                y = 55
        if keys[pygame.K_UP] :
            y -= 60
            if y<55:
                y=475
        if keys[pygame.K_z] and y == 55:
            pygame.mixer.music.load("C:/Users/Dimash/Desktop/Dimash2024PP2/lab7/JEVIL.mp3")
            pygame.mixer.music.play()
        if keys[pygame.K_z] and y == 115:
            pygame.mixer.music.load("C:/Users/Dimash/Desktop/Dimash2024PP2/lab7/BIG_SHOT.mp3")
            pygame.mixer.music.play()
        if keys[pygame.K_z] and y == 175:
            pygame.mixer.music.load("C:/Users/Dimash/Desktop/Dimash2024PP2/lab7/GHOST_FIGHT.mp3")
            pygame.mixer.music.play()
        if keys[pygame.K_z] and y == 235:
            pygame.mixer.music.load("C:/Users/Dimash/Desktop/Dimash2024PP2/lab7/MEGALOVANIA.mp3")
            pygame.mixer.music.play()
        if keys[pygame.K_z] and y == 295:
            pygame.mixer.music.load("C:/Users/Dimash/Desktop/Dimash2024PP2/lab7/METATON.mp3")
            pygame.mixer.music.play()
        if keys[pygame.K_z] and y == 355:
            pygame.mixer.music.load("C:/Users/Dimash/Desktop/Dimash2024PP2/lab7/MUFFET.mp3")
            pygame.mixer.music.play()
        if keys[pygame.K_z] and y == 415:
            pygame.mixer.music.load("C:/Users/Dimash/Desktop/Dimash2024PP2/lab7/PAPYRUS.mp3")
            pygame.mixer.music.play()
        if keys[pygame.K_z] and y == 475:
            pygame.mixer.music.load("C:/Users/Dimash/Desktop/Dimash2024PP2/lab7/UNDYNE.mp3")
            pygame.mixer.music.play()
        
        if keys[pygame.K_x]:
            pygame.mixer.music.stop()
    screen.fill((0, 0, 0))
    if y == 55:
        text1 = font.render("Jevil", True, (yellow))
    else:
        text1 = font.render("Jevil", True, (white)) 

    if y == 115:
        text2 = font.render("Big Shot", True, (yellow))
    else:
        text2 = font.render("Big Shot", True, (white))
    
    if y == 175:
        text3 = font.render("Ghost Fight", True, (yellow))
    else:
        text3 = font.render("Ghost Fight", True, (white)) 
    
    if y == 235:
        text4 = font.render("Megalovania", True, (yellow))
    else:
        text4 = font.render("Megalovania", True, (white)) 
    
    if y == 295:
        text5 = font.render("Metaton", True, (yellow))
    else:
        text5 = font.render("Metaton", True, (white)) 
    
    if y == 355:
        text6 = font.render("Muffet", True, (yellow))
    else:
        text6 = font.render("Muffet", True, (white)) 

    if y == 415:
        text7 = font.render("Papyrus", True, (yellow))
    else:
        text7 = font.render("Papyrus", True, (white)) 

    if y == 475:
        text8 = font.render("Undyne", True, (yellow))
    else:
        text8 = font.render("Undyne", True, (white)) 
           
    screen.blit(text1, (100, 60))
    screen.blit(text2, (100, 120))
    screen.blit(text3, (100, 180))
    screen.blit(text4, (100, 240))
    screen.blit(text5, (100, 300))
    screen.blit(text6, (100, 360))
    screen.blit(text7, (100, 420))
    screen.blit(text8, (100, 480))
    
    pygame.draw.polygon(screen, (255, 0, 0), [(300,y), (306,y), (306,y+3), (312,y+3), (312,y+6), (315,y+6), (315,y+12), (321,y+12), (321,y+6), (324,y+6), (324,y+3), (330,y+3), (330,y), (336,y), (336,y+3), (339,y+3), (339,y+6), (342,y+6), (342,y+27), (336,y+27), (336,y+33), (330,y+33), (330,y+39), (324,y+39), (324,y+45), (312,y+45), (312,y+39), (306,y+39), (306,y+33), (300,y+33), (300,y+27), (294,y+27), (294,y+6), (297,y+6), (297,y+3), (300,y+3)])
    pygame.display.flip()
    clock.tick(60)
