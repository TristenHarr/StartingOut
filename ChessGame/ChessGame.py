import pygame

pygame.init()


class Display:
    def __init__(self, width, height):
        self.Display = pygame.display.set_mode((width, height))

    def update(self):
        pygame.display.update()

    def type2(self, events):
        pass

    def type3(self, events):
        pass

    def type4(self, events):
        pass

    def type5(self, events):
        pass

    def type6(self, events):
        pass

    def getevent(self, events, event_type):
        if event_type == 1:
            pass
        elif event_type == 2:
            self.type2(events)
        elif event_type == 3:
            self.type3(events)
        elif event_type == 4:
            self.type4(events)
        elif event_type == 5:
            self.type5(events)
        elif event_type == 6:
            self.type6(events)

    def go(self):
        over = False
        while not over:
            for event in pygame.event.get():
                if event.type == 12:
                    over = True
                self.getevent(event.dict, event.type)


class Chess(Display):
    def __init__(self):
        super().__init__(600, 600)
        self.title = pygame.display.set_caption("Chess")
        self.background = self.Display.fill((0, 80, 10))
        self.moveprog = []
        self.turn = "WB"
        self.selection = None
        self.Clicked = pygame.image.load("Clicked.png")

    def showpieces(self):
        pass

    def updateboard(self):
        board = pygame.image.load("Board.png")
        self.Display.blit(board, (100, 100))
        self.showpieces()
        self.update()

    def mouseon(self, position):
        callitx = None
        callity = None
        my_ranges = [range(100, 150), range(150, 200),
                     range(200, 250), range(250, 300),
                     range(300, 350), range(350, 400),
                     range(400, 450), range(450, 500),
                     range(500, 550), range(550, 600)]
        for i in range(8):
            if position[0] in my_ranges[i]:
                callitx = i
            if position[1] in my_ranges[i]:
                callity = i
        return callitx, callity

    def checkpiece(self, current, request):
        pass

    def getpiece(self, current):
        pass

    def checkmate(self):
        pass

    def type5(self, events):
        self.moveprog.append(self.mouseon(events['pos']))
        self.selection = self.getpiece(self.moveprog[0])
        if self.selection == "":
            self.moveprog.append(self.moveprog[0])
        elif self.turn[0] != self.selection[0]:
            self.moveprog.append(self.moveprog[0])
        else:

            rectangle2 = pygame.Surface([50, 50]).convert()
            rectangle2.blit(self.Clicked, (0, 0))
            rectangle2.set_colorkey((0, 0, 255))
            self.Display.blit(rectangle2, (100 + self.moveprog[0][0] * 50, 100 + self.moveprog[0][1] * 50))
            pygame.display.update()
        if len(self.moveprog) == 2:
            self.checkpiece(self.selection, self.moveprog[0], self.moveprog[1])
            print(self.selection)
            print(self.moveprog[0])
            print(100 + self.moveprog[0][0] * 50, 100 + self.moveprog[0][1] * 50)
            # self.Display.blit(self.Clicked, (100+self.moveprog[0][0]*50, 100 + self.moveprog[0][1]*50))
            # pygame.display.update()
            done = self.checkmate()
            if done == "Black":
                print("BLACK WINS")
            elif done == "White":
                print("WHITE WINS")
            print(done)
            self.moveprog.clear()


class ChessBoard(Chess):
    def __init__(self):
        super().__init__()
        self.contents = {"0^0": "BROOK", "0^1": "BPAWN", "0^2": "", "0^3": "",
                         "0^4": "", "0^5": "", "0^6": "WPAWN", "0^7": "WROOK",
                         "1^0": "BKNIGHT", "1^1": "BPAWN", "1^2": "", "1^3": "",
                         "1^4": "", "1^5": "", "1^6": "WPAWN", "1^7": "WKNIGHT",
                         "2^0": "BBISHOP", "2^1": "BPAWN", "2^2": "", "2^3": "",
                         "2^4": "", "2^5": "", "2^6": "WPAWN", "2^7": "WBISHOP",
                         "3^0": "BKING", "3^1": "BPAWN", "3^2": "", "3^3": "",
                         "3^4": "", "3^5": "", "3^6": "WPAWN", "3^7": "WQUEEN",
                         "4^0": "BQUEEN", "4^1": "BPAWN", "4^2": "", "4^3": "",
                         "4^4": "", "4^5": "", "4^6": "WPAWN", "4^7": "WKING",
                         "5^0": "BBISHOP", "5^1": "BPAWN", "5^2": "", "5^3": "",
                         "5^4": "", "5^5": "", "5^6": "WPAWN", "5^7": "WBISHOP",
                         "6^0": "BKNIGHT", "6^1": "BPAWN", "6^2": "", "6^3": "",
                         "6^4": "", "6^5": "", "6^6": "WPAWN", "6^7": "WKNIGHT",
                         "7^0": "BROOK", "7^1": "BPAWN", "7^2": "", "7^3": "",
                         "7^4": "", "7^5": "", "7^6": "WPAWN", "7^7": "WROOK"}

    def checkmate(self):
        if "WKING" not in self.contents.values():
            return "Black"
        elif "BKING" not in self.contents.values():
            return "White"
        else:
            return False

    def turnswitch(self):
        self.turn = self.turn[::-1]

    def getpiece(self, position):
        piecepos = "{}^{}".format(position[0], position[1])
        return self.contents[piecepos]

    def w_pawn_check(self, current, request):
        a, b, c, d = current[0], current[1], request[0], request[1]
        if a == c and b - 1 == d and self.contents["{}^{}".format(c, d)] == "":
            return True
        elif b == 6 and a == c and b - 2 == d and self.contents["{}^{}".format(c, d)] == "":
            return True
        elif ((a - 1 == c) or (a + 1 == c)) and b - 1 == d and self.contents["{}^{}".format(c, d)] != "":
            return True

    def b_pawn_check(self, current, request):
        a, b, c, d = current[0], current[1], request[0], request[1]
        my_bool = self.contents["{}^{}".format(c, d)] == ""
        if a == c and b + 1 == d and my_bool:
            return True
        elif b == 1 and a == c and b + 2 == d and my_bool:
            return True
        elif ((a + 1 == c) or (a - 1 == c)) and b + 1 == d and not my_bool:
            return True

    def rook_check(self, current, request):
        if current[0] == request[0] and current[1] in range(0, 8):
            return True
        elif current[1] == request[1] and current[0] in range(0, 8):
            return True

    def knight_check(self, current, request):
        a, b, c, d = current[0], current[1], request[0], request[1]
        if a + 1 == c and b - 2 == d:
            return True
        elif a + 2 == c and b - 1 == d:
            return True
        elif a + 2 == c and b + 1 == d:
            return True
        elif a + 1 == c and b + 2 == d:
            return True
        elif a - 1 == c and b + 2 == d:
            return True
        elif a - 2 == c and b + 1 == d:
            return True
        elif a - 2 == c and b - 1 == d:
            return True
        elif a - 1 == c and b - 2 == d:
            return True
            # +2 +1, -2 -1, -1, -2

    def bishop_check(self, current, request):
        if abs(current[0] - request[0]) == abs(current[1] - request[1]):
            return True

    def queen_check(self, current, request):
        if self.bishop_check(current, request) or self.rook_check(current, request):
            return True

    def king_check(self, current, request):
        a, b, c, d = current[0], current[1], request[0], request[1]
        if abs(a - c) == 1 and b == d:
            return True
        elif abs(b - d) == 1 and a == c:
            return True
        elif abs(b - d) == 1 and abs(a - c) == 1:
            return True

    def blocked(self, current, request):
        a, b, c, d = current[0], current[1], request[0], request[1]
        movefrom = "{}^{}".format(a, b)
        moveto = "{}^{}".format(c, d)
        if self.contents[movefrom][0] == self.turn[0]:
            if self.contents[movefrom] != "" and self.contents[moveto] != "":
                if self.contents[movefrom][0] == self.contents[moveto][0]:
                    return True
            if a < c and b == d:
                for i in range(a + 1, c):
                    if self.contents["{}^{}".format(i, d)] != "":
                        return True
                else:
                    return False
            elif a > c and b == d:
                for i in range(c + 1, a):
                    if self.contents["{}^{}".format(i, d)] != "":
                        return True
                else:
                    return False
            elif a == c and b > d:
                for i in range(d + 1, b):
                    if self.contents["{}^{}".format(c, i)] != "":
                        return True
                else:
                    return False
            elif a == c and b < d:
                for i in range(b + 1, d):
                    if self.contents["{}^{}".format(c, i)] != "":
                        return True
                else:
                    return False
            elif self.bishop_check(current, request):
                if a < c and b < d:
                    for i in range(1, abs(a + 1 - c) + 1):
                        if self.contents["{}^{}".format(a + i, b + i)] != "":
                            return True
                    else:
                        return False
                elif a > c and b > d:
                    for i in range(1, abs(a + 1 - c) - 1):
                        if self.contents["{}^{}".format(a - i, b - i)] != "":
                            return True
                    else:
                        return False
                elif a > c and b < d:
                    for i in range(1, abs(a - c)):
                        if self.contents["{}^{}".format(a - i, b + i)] != "":
                            return True
                    else:
                        return False
                elif a < c and b > d:
                    for i in range(1, abs(a - c)):
                        if self.contents["{}^{}".format(a + i, b - i)] != "":
                            return True
                    else:
                        return False
        else:
            return True

    def showpieces(self):
        for item in self.contents:
            if self.contents[item] != '':
                x, y = item.split('^')
                renders = 100 + int(x) * 50, 100 + int(y) * 50
                the_picture = self.contents[item]
                the_pic = pygame.image.load("{}.png".format(the_picture))
                rectangle = pygame.Surface([50, 50]).convert()
                rectangle.blit(the_pic, (0, 0))
                rectangle.set_colorkey((0, 0, 255))
                self.Display.blit(rectangle, renders)

        self.update()

    def checkpiece(self, piece, current, request):
        if "PAWN" in piece:
            if piece[0] == "W":
                works = self.w_pawn_check(current, request)
                if works:
                    if not self.blocked(current, request):
                        self.contents["{}^{}".format(current[0], current[1])] = ""
                        self.contents["{}^{}".format(request[0], request[1])] = piece
                        self.turnswitch()
            elif piece[0] == "B":
                works = self.b_pawn_check(current, request)
                if works:
                    if not self.blocked(current, request):
                        self.contents["{}^{}".format(current[0], current[1])] = ""
                        self.contents["{}^{}".format(request[0], request[1])] = piece
                        self.turnswitch()
        else:
            if "ROOK" in piece:
                works = self.rook_check(current, request)
                if works:
                    if not self.blocked(current, request):
                        self.contents["{}^{}".format(current[0], current[1])] = ""
                        self.contents["{}^{}".format(request[0], request[1])] = piece
                        self.turnswitch()
            elif "KNIGHT" in piece:
                works = self.knight_check(current, request)
                if works:
                    if not self.blocked(current, request):
                        self.contents["{}^{}".format(current[0], current[1])] = ""
                        self.contents["{}^{}".format(request[0], request[1])] = piece
                        self.turnswitch()
            elif "BISHOP" in piece:
                works = self.bishop_check(current, request)
                if works:
                    if not self.blocked(current, request):
                        self.contents["{}^{}".format(current[0], current[1])] = ""
                        self.contents["{}^{}".format(request[0], request[1])] = piece
                        self.turnswitch()
            elif "QUEEN" in piece:
                works = self.queen_check(current, request)
                if works:
                    if not self.blocked(current, request):
                        self.contents["{}^{}".format(current[0], current[1])] = ""
                        self.contents["{}^{}".format(request[0], request[1])] = piece
                        self.turnswitch()
            elif "KING" in piece:
                works = self.king_check(current, request)
                if works and not self.blocked(current, request):
                    self.contents["{}^{}".format(current[0], current[1])] = ""
                    self.contents["{}^{}".format(request[0], request[1])] = piece
                    self.turnswitch()
        self.updateboard()



Game = ChessBoard()
Game.updateboard()
Game.go()
