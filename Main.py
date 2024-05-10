import pygame

#pygame Setup
pygame.init()
screen = pygame.display.set_mode((1200,720))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #filling Screen
    screen.fill("Blue")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
    