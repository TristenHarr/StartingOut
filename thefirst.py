import pygame
from LinkSprite import SpriteMove
SpriteSheet = SpriteMove.SpriteSheets
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
Over = False
LinkAll = SpriteSheet('LinkWalks.jpg')
Link = LinkAll.get_image(25, 0, 25, 25)
cls = 0
links = 25
def linkon(x, y):
    Link = LinkAll.get_image(links, 75, 25, 25)
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Clear = LinkAll.get_image(cls, 100, 25, 25)
    Link = LinkAll.get_image(links, 100, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Link = LinkAll.get_image(links, 125, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Link = LinkAll.get_image(links, 150, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Link = LinkAll.get_image(links, 175, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Link = LinkAll.get_image(links, 200, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Link = LinkAll.get_image(links, 225, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Link = LinkAll.get_image(links, 250, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Link = LinkAll.get_image(links, 275, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)
    Link = LinkAll.get_image(links, 300, 25, 25)
    gameDisplay.blit(Clear, (x, y))
    y += 5
    gameDisplay.blit(Link, (x, y))
    pygame.display.update()
    pygame.time.wait(75)

x = 100
y = 100
lastevent = []
while not Over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Over = True
        if event.type == 2:
            keypress = event.dict['key']
            options = [273,274,275,276]
            if keypress in options:
                if keypress == options[0]:
                    call = "up"
                    y -= 5
                if keypress == options[1]:
                    call = "down"
                    y += 5
                if keypress == options[2]:
                    call = "right"
                    x += 5
                if keypress == options[3]:
                    call = 'left'
                    x -= 5
    gameDisplay.fill(white)
    linkon(x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()