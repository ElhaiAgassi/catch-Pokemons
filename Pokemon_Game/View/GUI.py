import pygame
from pygame import gfxdraw

from Pokemon_Game.Controller.client import Client

WIDTH, HEIGHT = 960, 600
BLACK, WHITE, DARKBLUE, RED, COUT = (
                                        0, 0, 0), (255, 255, 255), (25, 25, 112), (210, 56, 23), (248, 244, 243)
clock = pygame.time.Clock()
pygame.init()
''' ----------------------- Image -------------------------'''
Ash = 'View/media/Ash.png'
Pikachu = 'View/media/Pikachu.png'
Pokeball = 'View/media/Pokeball.png'
Background = 'View/media/Background.jpg'
Charmander = 'View/media/Charmander.png'
Brock = 'View/media/Brock.png'
Misty = 'View/media/Misty.png'
'''-------------------------------------------------------'''
pygame.mixer.init()
radius = 15
FONT = pygame.font.SysFont('Arial', 20, bold=True)
MOVE_FONT = pygame.font.SysFont('Verdana', 25)
EXIT_FONT = pygame.font.SysFont('Verdana', 40)
pygame.display.set_caption("Pokemon is better than Digimon")
screen = pygame.display.set_mode((WIDTH, HEIGHT), depth=32, flags=pygame.RESIZABLE)
buttonRec = pygame.Rect((2, 2), (58, 38))
buttonPress = False


class GUI:
    def __init__(self, myGame):
        self.myGame = myGame
        self.min_x = float('inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')
        self.max_x = float('-inf')

        for n in self.myGame.Graph.nodes.values():
            x = n.pos[0]
            y = n.pos[1]
            self.min_x = min(self.min_x, x)
            self.min_y = min(self.min_y, y)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)
        self.player = []
        self.player.append(pygame.image.load(Ash))
        self.player.append(pygame.image.load(Misty))
        self.player.append(pygame.image.load(Brock))

        self.background = pygame.image.load(Background)
        self.Pokeball = pygame.transform.scale(pygame.image.load(Pokeball), (30, 30))
        self.Ash = pygame.transform.scale(pygame.image.load(Ash), (30, 58))
        self.Pikachu = pygame.image.load(Pikachu)
        self.Charmander = pygame.image.load(Charmander)

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, screen.get_width() - 50, self.min_x, self.max_x)

        if y:
            return self.scale(data, 50, screen.get_height() - 50, self.min_y, self.max_y)

    def drawPokadurs(self):
        graph_ = self.myGame.Graph
        for n in graph_.nodes.values():
            x = n.pos[0]
            y = n.pos[1]
            x = self.my_scale(x, x=True)
            y = self.my_scale(y, y=True)
            gfxdraw.filled_circle(screen, int(x), int(y),
                                  radius, pygame.Color(64, 80, 174))
            screen.blit(self.Pokeball, (int(x) - 15, int(y) - 15))

            id = FONT.render(str(n.key), True, pygame.Color(BLACK))
            rect = id.get_rect(center=(x, y))
            screen.blit(id, rect)

    """"dont forget To change for the pokadurim """

    def draw_edges(self):
        edges = self.myGame.Graph.edges
        for e in edges.keys():
            # find the edge nodes
            src = self.myGame.Graph.nodes[e[0]]
            dest = self.myGame.Graph.nodes[e[1]]

            X_src = self.my_scale(src.pos[0], x=True)
            Y_src = self.my_scale(src.pos[1], y=True)
            X_dest = self.my_scale(dest.pos[0], x=True)
            Y_dest = self.my_scale(dest.pos[1], y=True)
            # draw the line
            pygame.draw.line(screen, pygame.Color(61, 72, 126),
                             (X_src, Y_src), (X_dest, Y_dest), width=5)

    def draw_agent(self):
        agents = self.myGame.agents
        for i, a in enumerate(agents):
            x, y = a.pos[0], a.pos[1]
            x = self.my_scale(float(x), x=True)
            y = self.my_scale(float(y), y=True)
            screen.blit(self.player[i], (int(x) - 18, int(y) - 18))

    def draw_pokemons(self):
        pokemons = self.myGame.pokemons
        for p in pokemons:
            x, y = p.pos[0], p.pos[1]
            x = self.my_scale(float(x), x=True)
            y = self.my_scale(float(y), y=True)
            if p.type == 1:
                screen.blit(self.Pikachu, (int(x) - 18, int(y) - 18))
            else:
                screen.blit(self.Charmander, (int(x) - 18, int(y) - 18))

    def draw_move_grade(self, client: Client):
        info = client.get_info().split(",")
        move = int(info[2].split(":")[1])
        grade = int(info[3].split(":")[1])
        moves = MOVE_FONT.render("Move: " + str(move), True, pygame.Color(DARKBLUE))
        grades = MOVE_FONT.render(
            "Grade: " + str(grade), True, pygame.Color(DARKBLUE))
        screen.blit(moves, (10, screen.get_height() - 30))
        screen.blit(
            grades, ((screen.get_width() - 140, screen.get_height() - 30)))

    def draw_Buttons(self):
        global buttonRec
        pygame.draw.rect(screen, (COUT), buttonRec)
        button_text = MOVE_FONT.render("Exit", True, (RED))
        screen.blit(button_text, (buttonRec.x + 5, buttonRec.y + 5))

    def run(self, client: Client):
        global buttonRec
        global buttonPress
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                print(client.get_info())
                exit(0)
                return False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if buttonRec.collidepoint(e.pos):
                    buttonPress = not buttonPress
                    if buttonPress:
                        pygame.quit()
                        exit(0)

        background = pygame.transform.scale(
            self.background, (screen.get_width(), screen.get_height()))
        screen.blit(background, [0, 0])
        self.draw_edges()
        self.drawPokadurs()
        self.draw_pokemons()
        self.draw_agent()
        self.draw_Buttons()
        self.draw_move_grade(client)
        pygame.display.update()
