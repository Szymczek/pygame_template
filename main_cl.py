import pygame
from config import *


class Game:
    def __init__(self):
        # initialize game window, etc
        self.all_sprites = pygame.sprite.Group()
        self.playing = True
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.run()

    def run(self):
        # Game loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(RED)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_go_screen()
pygame.quit()
