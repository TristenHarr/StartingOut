import pygame
pygame.init()

class display(object):

    def __init__(self, width, height):
        self.Display = pygame.display.set_mode((width, height))
        self.title = pygame.display.set_caption("")
        self.background = self.Display.fill((0, 80, 10))
        self.update = pygame.display.update()
        self.click = False
        self.clicked = None
        self.clickhist = []
        self.board = pygame.image.load("Board.png")
        self.clicker = pygame.image.load("Clicked.png")
        self.show = self.Display.blit(self.board, (100, 100))


    def getevent(self, events, event_type):
        # print(events, event_type)
        callitx = None
        callity = None
        if event_type == 1:
            pass
        elif event_type == 2:
            print(events)
            self.show
            pygame.display.update()
        elif event_type == 3:
            print(events)
        elif event_type == 4:
            pass
        elif event_type == 5:
            self.click = True
            clicked = events["button"]
            if clicked == 1:
                but = "LEFT"
            elif clicked == 3:
                but = "RIGHT"
            self.clicked = [but, events['pos']]
            print(events['pos'])
            my_ranges = [range(100,150),range(150,200),range(200,250),range(250,300),range(300,350),range(350,400),range(400,450),range(450,500),range(500,550),range(550,600)]
            for i in range(8):
                if events['pos'][0] in my_ranges[i]:
                    callitx = i
                if events['pos'][1] in my_ranges[i]:
                    callity = i
            print(callitx, callity)
            if None not in [callitx, callity]:
                myclicked = (100+50*callitx, 100+50*callity)
                self.Display.blit(self.board, (100,100))
                self.Display.blit(self.clicker, myclicked)
                pygame.display.update()
            self.clickhist.append([events['button'], events['pos']])
        elif event_type == 6:
            self.click = False


    def go(self):
        Over = False
        while not Over:
            for event in pygame.event.get():
                if event.type == 12:
                    Over = True
                self.getevent(event.dict, event.type)
            if self.click == True:
                pass




Game = display(600,600)

Game.go()
