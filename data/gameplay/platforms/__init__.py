import pygame
from data.backgrounds import Backgound as Back
from data.gameplay.platforms.types import platformP1
from data.gameplay.platforms.types import platformP2
#from data.gameplay.plataforms.type import plataformP3
#from data.gameplay.plataforms.type import plataformP4


class Plataform:
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        # self.display = pygame.Surface((300,200))
        self.game_map = self.load_map()
        self.background = Back(screen)     

    def load_map(self):
        file = open('data/gameplay/platforms/p'+str(self.nivel)+ '.txt', 'r')
        data = file.read()
        file.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map

    def settingPlataform(self, scroll):
        self.background.movingBackgourndGamePlay(1)
        if(self.nivel <= 1):
            return platformP1(self.game_map, self.screen, scroll)
        elif(self.nivel == 2):
            return platformP2(self.game_map, self.screen, scroll)
        elif(self.nivel ==3):
            return platformP1(self.game_map,self.screen,scroll)
        '''elif(self.nivel ==4):
            return platformP3(self.game_map,self.screen,scroll)'''