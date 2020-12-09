import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back
from data.textInput import Textinput as textInput

class CreateUserMenu:
    def __init__(self, screen, nrImage, painelState, nivel):
        pygame.init()
        self.screen = screen
        self.painelState = painelState
        self.background = Back(nrImage, painelState, nivel)
        self.painel = pygame.image.load("resources/image/menu/painel.png").convert_alpha()
        self.title = pygame.image.load("resources/image/title/MinoTrolls1.png").convert_alpha()
        self.createText = "Enter a user name"
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = textInput()
        self.menuControl = 250
        self.count = 0
        self.timeEfect = 0
        self.buttoms = ['createuser','back']
        self.currentButtom = self.buttoms[0]
        self.allButtom = []
        self.allPosition = [(260, 250), (260, 300)]
        self.displayButtoms()

    # Method to render all the components in the screen
    def displayButtoms(self):
        self.allButtom = []
        for buttom in self.buttoms:
            if(self.currentButtom == buttom):
                if (self.timeEfect == 30):
                    img = pygame.image.load("resources/image/menu/createUser/"+buttom+"1.png").convert_alpha()
                    self.timeEfect = 0
                else:
                    img = pygame.image.load("resources/image/menu/createUser/"+buttom+"2.png").convert_alpha()
                    self.timeEfect += 1
            else:
                img = pygame.image.load("resources/image/menu/createUser/"+buttom+"0.png").convert_alpha()
            self.allButtom.append(img)

    def settingUserName(self, event):
        self.background.settingBackground(self.screen)
        self.screen.blit(self.painel, (105, 70))
        self.screen.blit(self.title, (275, 90))
        line = self.font.render(self.createText, True, (0, 0,0))
        self.screen.blit(line, (265, 150))
        self.text.settingInputText(self.screen, event)

        # Controling menu buttons efects
        if (self.menuControl == 250):
            self.currentButtom = self.buttoms[0]
        else:
            self.currentButtom = self.buttoms[1]

        self.displayButtoms()
        [self.screen.blit(img, pos) for img, pos in zip(self.allButtom, self.allPosition)]
        



    # Method to move in this menu and return the choose
    def drawUserMenu(self, event):
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[K_DOWN]):
            pygame.time.delay(100)
            if(self.menuControl == 300):
                self.menuControl = 250
            else:
                self.menuControl += 50
        elif(pressed_keys[K_UP]):
            pygame.time.delay(100)
            if(self.menuControl == 250):
                self.menuControl = 250
            else:
                self.menuControl -= 50

        self.count += 1
        if((pressed_keys[K_x])and(self.menuControl==250)and(self.count >= 5)):
            self.count = 0
            return 3
        elif((pressed_keys[K_x])and(self.menuControl==300)and(self.count >= 5)):
            self.count = 0
            return 1
        self.settingUserName(event)
        return 2