import sys, pygame, os
pygame.init()

def load_image(name):
    fullname = os.path.join('C:/Users/ccp/Documents/GitHub/One_heart_to_break/Images/', name)
    image = pygame.image.load(fullname)
    return image

def position_image(name,x,y):
    name.center = (x,y)
    return name

def left_mouse_Clicked():
    mouseState = pygame.mouse.get_pressed()[0]
    return mouseState

def getMousePos():
    mousePos = pygame.mouse.get_pos()
    return mousePos

def createGamescreen():
    return 0

def run_game():
    SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
    BG_COLOR = 0, 0, 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    Menu = load_image('menu.png')
    Start = load_image("start.png")
    Exit = load_image("exit.png")
    MenuRect = Menu.get_rect()
    StartRect = Start.get_rect()
    ExitRect = Exit.get_rect()
    position_image(MenuRect,SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    position_image(StartRect, SCREEN_WIDTH/2,(SCREEN_HEIGHT/2)-100)
    position_image(ExitRect, SCREEN_WIDTH/2,600)
    menuState = 1
    gameState = 0
    while True:
            # Limit frame speed to 50 FPS
            #
            time_passed = clock.tick(50)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                if ExitRect.collidepoint(x, y):
                    exit_game()
                if StartRect.collidepoint(x,y):
                    menuState = 0
            if menuState == 1:
                screen.blit(Menu, MenuRect)
                screen.blit(Start, StartRect)
                screen.blit(Exit, ExitRect)
                pygame.display.flip()
            if menuState == 0:
                pygame.display.flip()
                

def exit_game():
    sys.exit()


run_game()