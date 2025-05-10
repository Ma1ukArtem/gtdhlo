import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Моя перша програма на пайгейм")
screen.fill((255,255,255))
house_rect=pygame.Rect(100,100,200,200)
pygame.draw.rect(screen,(255,0,0),house_rect)




while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()

    pygame.display.update()        

