import pygame
from pygame import *
from pygame import gfxdraw
from client import Client
from myGame import *

WIDTH, HEIGHT = 1080, 720

Ash = 'client_python/GUI_media/Ash.jpg'
Pikachu = 'client_python/GUI_media/Pikachu.png'
Pokeball = 'client_python/GUI_media/Pokeball.png'
Background = 'client_python/GUI_media/Background.jpg'
pygame.init()
mixer.init()
radius = 28


class GUI():
    def __init__(self, myGame: myGame, client=Client) -> None:
        self.myGame = myGame
        self.graph = myGame.graph
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        clock = pygame.time.Clock()
        FONT = pygame.font.SysFont('Arial', 20, bold=True)
        pygame.font.init()
        """init images"""
        self.background = image.load(Background)
        self.Pokeball = pygame.transform.scale(image.load(Pokeball), (25, 25))
        self.Ash = pygame.transform.scale(image.load(Ash), (25, 25))
        self.Pikachu = image.load(Pikachu)

        self.screen.fill(Color(0, 0, 0))

        self.min_x = float('inf')
        self.min_y = float('inf')
        self.max_x = float('-inf')
        self.max_y = float('-inf')

        for n in self.graph.nodes.values():
            x = n.pos[0]
            y = n.pos[1]

            self.min_x = min(self.min_x, x)
            self.min_y = min(self.min_y, y)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, x)

        # self.quit_button = Button(Color(61, 72, 126),)
        # self.move_button = Button((0, 0, 0), 142, 2, 70, 20, 'MOVES')
        # self.grade_button = Button((0, 0, 0), 212, 2, 70, 20, 'GRADE')

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, self.min_y, self.max_y)

    def drawPokadurs(self):

        for n in self.graph.nodes.values():
            x = self.my_scale(n.pos[0], x=True)
            y = self.my_scale(n.pos[1], y=True)

            gfxdraw.filled_circle(self.screen, int(x), int(y), radius, Color(64, 80, 174))
            gfxdraw.aacircle(self.screen, int(x), int(y), radius, Color(255, 255, 255))

        """"dont forget To change for the pokadurim """

    def draw_edges(self):
        edges = self.graph.edges
        for e in edges.keys():
            # find the edge nodes

            src = self.graph.nodes[e[0]]
            dest = self.graph.nodes[e[1]]

            X_src = self.my_scale(src.pos[0], x=True)
            Y_src = self.my_scale(src.pos[1], y=True)
            X_dest = self.my_scale(dest.pos[0], x=True)
            Y_dest = self.my_scale(dest.pos[1], y=True)
            # draw the line
            pygame.draw.line(self.screen, Color(61, 72, 126), (X_src, Y_src), (X_dest, Y_dest), width= 5)

    def draw_agent(self):
        agents = self.myGame.agents
        for a in agents:
            x, y = a.pos[0], a.pos[1]
            x = self.my_scale(float(x), x=True)
            y = self.my_scale(float(y), y=True)
            # self.screen.blit(self.Ash, (int(x) - 28, int(y) - 28))

    def draw_pokemons(self):
        pokemons = self.myGame.pokemons
        for p in pokemons:
            x, y = p.pos[0], p.pos[1]
            x = self.my_scale(p.pos[0], x=True)
            y = self.my_scale(p.pos[1], y=True)
            # self.screen.blit(self.Pikachu, (int(x) - 15, int(y) - 15))

    def draw_move(self, move):
        number_of_move = pygame.font.SysFont('Verdana', 30).render("Move: " + str(move), True, Color(100, 100, 100))
        self.screen.blit(number_of_move, (self.screen.get_width() - 110, self.screen.get_height() - 30))

    def draw_Buttons(self):
        pygame.draw.rect(self.screen, button.color, button.rect)
        button_text = pygame.font.SysFont('Ariel', 30).render("Exit", True, (210, 56, 23))
        self.screen.blit(button_text, (button.rect.x + 20, button.rect.y + 10))

    def run(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                return False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(e.pos):
                    button.press()
                    if button.pressed:
                        pygame.quit()
                        exit(0)

        self.screen.fill(Color(0, 0, 0))  # /??
        background = transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background, [0, 0])
        self.draw_Buttons()
        self.draw_edges()
        self.draw_agent()
        self.draw_pokemons()
        self.drawPokadurs()
        display.update()


class Button:

    def __init__(self, color, rect: pygame.Rect):  ## rect?
        self.color = color
        self.rect = rect
        self.pressed = False

    def press(self):
        self.pressed = not self.pressed


button = Button(color=(0, 0, 0), rect=pygame.Rect((10, 10), (100, 50)))
