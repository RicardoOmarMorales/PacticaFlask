import py

Blanco = (255,255,255)
negro = (0,0,0)
 

pygame.init ()
superficie = pygame.display.set_mode ((800,500))
pygame.display.set_caption('serpiente')
 
 
gameExit = False
 
move_x = 300
move_y = 300
 
while not gameExit:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            gameExit = True
 
        if event.type == pygame.KEY_DOWN:
            
#        if event.key == pygame.K_LEFT:
            move_x -= 10
        if event.key == pygame.K_RIGHT:
              move_x += 10
 
 
    s<uperficie.fill (Blanco)
    pygame.draw.rect(superficie,negro, [move_x, mover_y,10,10])
    pygame.display.update ()
 
    pygame.quit ()
    quit ()