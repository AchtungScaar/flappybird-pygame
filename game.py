import pygame, sys

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

bd = pygame.image.load('assets/nightbackdrop1.jpg')
bd = pygame.transform.scale2x(bd)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bd,(0,0))

    pygame.display.update()
    clock.tick(120)