import pygame , sys
import random



pygame.init()
pygame.mouse.set_visible(False)

#General Variables
WIDTH = 1280
HEIGHT = 720
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
VELO_LAND = 1
VELO_WATER = random.randint(1,3)
WHITE = (255,255,255)
DUCKS_LIST = []


#Game Assets
WOOD_SRFC = pygame.image.load("shooting range assets/Wood_BG.png")
WATER_SRFC = pygame.image.load("shooting range assets/Water_BG.png")
LAND_SRFC = pygame.image.load("shooting range assets/Land_BG.png")
CLOUD1_SRFC = pygame.image.load("shooting range assets/Cloud1.png")
CLOUD2_SRFC = pygame.image.load("shooting range assets/Cloud2.png")
CROSSHAIR_SRFC = pygame.image.load("shooting range assets/crosshair.png")
DUCK_SRFC = pygame.image.load("shooting range assets/duck.png")
WINING_TEXT = pygame.font.Font(None,60)
TEXT_SRFC = WINING_TEXT.render("You won! You destroyed all the ducks!", True, WHITE)
TEXT_RECT = TEXT_SRFC.get_rect(center = (WIDTH/2 , HEIGHT/2 ))

#POS
LAND_SRFC_Y = (HEIGHT - 150)
WATER_SRFC_Y = (600)

for ducks in range(12):
    DUCK_POSITION_X = random.randrange(50, 1200)
    DUCK_POSITION_Y = random.randrange(40, 660)
    DUCK_RECT = DUCK_SRFC.get_rect(center=(DUCK_POSITION_X, DUCK_POSITION_Y))
    DUCKS_LIST.append(DUCK_RECT)

def game_blits():
    SCREEN.blit(WOOD_SRFC, (0, 0))
    SCREEN.blit(LAND_SRFC, (0, LAND_SRFC_Y))
    SCREEN.blit(WATER_SRFC, (0,WATER_SRFC_Y))
    SCREEN.blit(CLOUD1_SRFC, (WIDTH - 600, CLOUD1_SRFC.get_height()))
    SCREEN.blit(CLOUD2_SRFC, (WIDTH/2 - 500, CLOUD1_SRFC.get_height()))
    SCREEN.blit(CLOUD1_SRFC, (WIDTH - 40, CLOUD1_SRFC.get_height() + 100))
    SCREEN.blit(CLOUD2_SRFC, (WIDTH / 4 , CLOUD1_SRFC.get_height() + 100 ))

    for DUCK_RECT in DUCKS_LIST:
        SCREEN.blit(DUCK_SRFC,DUCK_RECT)

    if len(DUCKS_LIST) <= 0:
        SCREEN.blit(TEXT_SRFC, TEXT_RECT)

    SCREEN.blit(CROSSHAIR_SRFC, CROSSHAIR_RECT)


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            CROSSHAIR_RECT = CROSSHAIR_SRFC.get_rect(center = event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for index , DUCK_RECT in enumerate(DUCKS_LIST):
                if DUCK_RECT.collidepoint(event.pos):
                    del DUCKS_LIST[index]


    LAND_SRFC_Y -= VELO_LAND
    if LAND_SRFC_Y <= 520 or LAND_SRFC_Y >= 600:
        VELO_LAND *= -1

    WATER_SRFC_Y -= VELO_WATER
    if WATER_SRFC_Y <= 580 or WATER_SRFC_Y >= 695:
        VELO_WATER *= -1

    game_blits()
    pygame.display.update()
    CLOCK.tick(FPS)
