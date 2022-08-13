import pygame
from threading import Thread
from time import sleep
from random import choice, randint
pygame.init()
x = 200
y = 350
x_cube = 600
y_cube = 350
x_tree = randint(610, 800)
y_tree = 336
x_bush = randint(610, 1000)
y_bush = 359
x_stone = randint(610, 1000)
y_stone = 358
x_spells = 700
y_spells = 350
j_t = 0
list_colors = [(255, 0, 0), (0, 255, 0),
(0, 0, 255), (233, 130, 0), (0, 130, 255)]
list_colors_spells = [(255, 0, 0), (0, 255, 0),
(0, 0, 255)]
more_life = 0


def jump():
    global y

    c_j = 0.001
    if event.key == pygame.K_SPACE:
        for y_p in range(1, 38):
            y -= y_p / 10
            sleep(0.004 - c_j)
        for y_p in range(1, 38):
            y += y_p / 10
            sleep(0.003)
            
color = (255, 130, 0)
color_spells = (0, 255, 0)
veloct_cube = 5
veloct_tree = 5
veloct_bush = 5
veloct_stone = 5
veloct_spells = 5
gm_ovr_jmp = False
loc_g_m_x = -50
loc_g_m_y = -50
one = 0
def spell():
    global color_spells
    global more_life
    global one

    if color_spells == (255, 0, 0):
        more_life += 1


while True:   
    window = pygame.display.set_mode((600,400))
    window.fill(color=(255, 255, 255))
    cube_cube = pygame.draw.rect(window, color, pygame.Rect(x_cube, y_cube, 10, 10))
    pygame.draw.line(window, (0, 255, 0), (0, 383), (600, 383), 33)
    im_tree = pygame.image.load('project07/tree_bush.png')
    imt_tree = pygame.transform.scale(im_tree, (30, 33))
    window.blit(imt_tree, (x_tree, y_tree))
    bush = pygame.image.load('project07/bush.png')
    bush_scl = pygame.transform.scale(bush, (10, 10))
    window.blit(bush_scl, (x_bush, y_bush))
    stone = pygame.image.load('project07/stone.png')
    stone_scl = pygame.transform.scale(stone, (10, 10))
    window.blit(stone_scl, (x_stone, y_stone))
    x_cube -= veloct_cube
    x_tree -= veloct_tree
    x_bush -= veloct_bush
    x_stone -= veloct_stone
    x_spells -= veloct_spells
    font = pygame.font.SysFont(None, 40)
    str_gm_ov = font.render('Game over, Enter to try again', True, (255,0,0))
    window.blit(str_gm_ov, (loc_g_m_x, loc_g_m_y))
    if x_spells <= - 15:
        x_spells = randint(610, 1000)
        color_spells = choice(list_colors_spells)
    if x_stone <= -15:
        x_stone = randint(610, 1000)
    if x_bush <= -15:
        x_bush = randint(610, 1000)
    if x_tree <= -15:
        x_tree = randint(610, 800)
    if x_cube <= 0:
        color = choice(list_colors)
        x_cube = 650
    cube_orange = pygame.draw.rect(window, (255, 100, 0), pygame.Rect(x, y, 20, 20))
    cube_spells = pygame.draw.rect(window, (color_spells), pygame.Rect(x_spells, y_spells, 15, 15))
    pygame.display.flip()
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    #if keys[pygame.K_d]:
    #    x += vel_x
    #if keys[pygame.K_a]:
    #    x -= vel_x
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gm_ovr_jmp == False:
                Thread(target=jump).start()
            if event.key == pygame.K_RETURN:
                veloct_cube = 5
                veloct_tree = 5
                veloct_bush = 5
                veloct_stone = 5
                loc_g_m_x = -50
                loc_g_m_y = -50
                gm_ovr_jmp = False

                
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    if cube_orange.colliderect(cube_cube):
        print(more_life)
        if more_life == 0:
            veloct_cube = 0
            veloct_tree = 0
            veloct_bush = 0
            veloct_stone = 0
            gm_ovr_jmp = True
            loc_g_m_x = 100
            loc_g_m_y = 180
            x_tree = randint(610, 800)
            x_cube = 650
            x_bush = randint(610, 1000)
            x_stone = randint(610, 1000)
        if more_life > 0:
            more_life -= 1
            print(more_life)
    if cube_orange.colliderect(cube_spells):
        spell()
        
    if x >= 600:
        x = 570
    elif x <= 0:
        x = 5
    if y >= 350:
        y = 350
    elif y <= 0:
        y = 5
   