import pygame
from LinkSprite import SpriteMove
pygame.init()
pygame.event.set_blocked(pygame.MOUSEMOTION)

class display(object):
    def __init__(self, width, height):
        self.Display = pygame.display.set_mode((width, height))
        self.title = pygame.display.set_caption("")
        self.background = self.Display.fill((0, 0, 255))
        self.update = pygame.display.update()
        self.click = False
        self.clicked = None
        self.clickhist = []
        self.S = SpriteMove.SpriteSheets
        self.LinkAll = self.S("Link35F.png")
        self.LinkPos = [200,200]
        self.move = False
        self.currentstate = 0
    def movelink(self, keypress, move, linksizex, linksizey):
        options = [273, 274, 275, 276]
        if keypress in options:
            Clear = self.LinkAll.get_image(0, 0, linksizex, linksizey)
            if keypress == options[0]:
                linkx = 3*linksizex
                linky = 2*linksizey
                for i in range(10):
                    Link = self.LinkAll.get_image(linky, linkx, linksizex, linksizey)
                    self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
                    self.LinkPos[1] -= move
                    self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
                    self.background = self.Display.fill((0, 0, 255))
                    self.Display.blit(Link, (self.LinkPos[0], self.LinkPos[1]))
                    linkx += linksizex
                    pygame.display.update()
                    pygame.time.wait(50)
            elif keypress == options[1]:
                self.move = "down"
                linkx = 3*linksizex
                linky = linksizey
                for i in range(10):
                    Link = self.LinkAll.get_image(linky, linkx, linksizex, linksizey)
                    self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
                    self.LinkPos[1] += move
                    self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
                    self.background = self.Display.fill((0, 0, 255))
                    self.Display.blit(Link, (self.LinkPos[0], self.LinkPos[1]))
                    linkx += linksizex
                    pygame.display.update()
                    pygame.time.wait(50)
            elif keypress == options[2]:
                self.move = "right"
                linkx = 3*linksizex
                linky = 4*linksizey
                for i in range(10):
                    Link = self.LinkAll.get_image(linky, linkx, linksizex, linksizey)
                    self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
                    self.LinkPos[0] += move
                    self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
                    self.background = self.Display.fill((0, 0, 255))
                    self.Display.blit(Link, (self.LinkPos[0], self.LinkPos[1]))
                    linkx += linksizex
                    pygame.display.update()
                    pygame.time.wait(50)
            elif keypress == options[3]:
                self.move = "left"
                linkx = 3*linksizex
                linky = 3*linksizey
                for i in range(10):
                    Link = self.LinkAll.get_image(linky, linkx, linksizex, linksizey)
                    self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
                    self.LinkPos[0] -= move
                    self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
                    self.background = self.Display.fill((0, 0, 255))
                    self.Display.blit(Link, (self.LinkPos[0], self.LinkPos[1]))
                    linkx += linksizex
                    pygame.display.update()
                    pygame.time.wait(50)
            return "DONE"
    # def idlelink(self, keypress, move, linksizex, linksizey):
    #     options = [273, 274, 275, 276]
    #     if keypress in options:
    #         Clear = self.LinkAll.get_image(0, 0, linksizex, linksizey)
    #         if keypress == options[0]:
    #             linkx = 3 * linksizex
    #             linky = 2 * linksizey
    #             for i in range(10):
    #                 Link = self.LinkAll.get_image(linky, linkx, linksizex, linksizey)
    #                 self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
    #                 self.LinkPos[1] -= move
    #                 self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
    #                 self.background = self.Display.fill((0, 0, 255))
    #                 self.Display.blit(Link, (self.LinkPos[0], self.LinkPos[1]))
    #                 linkx += linksizex
    #                 pygame.display.update()
    #                 pygame.time.wait(75)
    #         elif keypress == options[1]:
    #             self.move = "down"
    #             linkx = 3 * linksizex
    #             linky = linksizey
    #             for i in range(10):
    #                 Link = self.LinkAll.get_image(linky, linkx, linksizex, linksizey)
    #                 self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
    #                 self.LinkPos[1] += move
    #                 self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
    #                 self.background = self.Display.fill((0, 0, 255))
    #                 self.Display.blit(Link, (self.LinkPos[0], self.LinkPos[1]))
    #                 linkx += linksizex
    #                 pygame.display.update()
    #                 pygame.time.wait(75)
    #         elif keypress == options[2]:
    #             self.move = "right"
    #             linkx = 3 * linksizex
    #             linky = 4 * linksizey
    #             for i in range(10):
    #                 Link = self.LinkAll.get_image(linky, linkx, linksizex, linksizey)
    #                 self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
    #                 self.LinkPos[0] += move
    #                 self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
    #                 self.background = self.Display.fill((0, 0, 255))
    #                 self.Display.blit(Link, (self.LinkPos[0], self.LinkPos[1]))
    #                 linkx += linksizex
    #                 pygame.display.update()
    #                 pygame.time.wait(75)
    #         elif keypress == options[3]:
    #             self.move = "left"
    #             linkx = 3 * linksizex
    #             linky = 3 * linksizey
    #             for i in range(10):
    #                 Link = self.LinkAll.get_image(linky, linkx, linksizex, linksizey)
    #                 self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
    #                 self.LinkPos[0] -= move
    #                 self.Display.blit(Clear, (self.LinkPos[0], self.LinkPos[1]))
    #                 self.background = self.Display.fill((0, 0, 255))
    #                 self.Display.blit(Link, (self.LinkPos[0], self.LinkPos[1]))
    #                 linkx += linksizex
    #                 pygame.display.update()
    #                 pygame.time.wait(75)
    #         return "DONE"

    def getevent(self, events, event_type):
        # print(events, event_type)
        if event_type == 1:
            pass
        elif event_type == 2:
            print(events, event_type)
            call = None
            keypress = events['key']
            options = [273, 274, 275, 276]
            if keypress in options:
                Answer = self.movelink(keypress, 4, 40, 40)

                print(pygame.KEYDOWN)
        elif event_type == 3:
            print(events, event_type)
            keypress = events['key']
            options = [273, 274, 275, 276]
            if keypress in options:
                # Answer = self.idlelink(keypress, 0, 40, 40)
                # print(Answer)
                pass

        elif event_type == 4:
            print(events, event_type)
        elif event_type == 5:
            print(events, event_type)
            self.click = True
            clicked = events["button"]
            if clicked == 1:
                but = "LEFT"
            elif clicked == 3:
                but = "RIGHT"
            self.clicked = [but, events['pos']]
            self.clickhist.append([events['button'], events['pos']])
        elif event_type == 6:
            print(events, event_type)
            self.click = False

    def go(self):
        Over = False
        while not Over:
            for event in pygame.event.get():
                if event.type == 12:
                    Over = True
                self.getevent(event.dict, event.type)




screen = display(800,600)
screen.go()
pygame.quit()