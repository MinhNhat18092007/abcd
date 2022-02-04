import pygame, sys, random
#TẠo hàm cho trò 
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop =(500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop =(500,random_pipe_pos-650))
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes :
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600 :
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >=650:
            return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement*4,1)
    return new_bird
pygame.init()
screen= pygame.display.set_mode((432,768))
clock = pygame.time.Clock() 
# Tạo các biến của trò 
gravity = 0.25
bird_movement = 0
game_active = True
#background
bg = pygame.image.load('assets/background-night.png').convert() 
bg = pygame.transform.scale2x(bg) 
#floor
floor = pygame.image.load('assets/floor.png')
floor = pygame.transform.scale2x(floor) 
floor_x_pos = 0
#make bird
bird = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
bird = pygame.transform.scale2x(bird) 
bird_rect = bird.get_rect(center = (100,384))
#make ống
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list =[]
#make timer
spawnpipe= pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200) 
pipe_height = [200,300,400]
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement =-11
            if event.key == pygame.K_SPACE and game_active==False:
                game_active =True
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_movement = 0
         if event.type == spawnpipe:
             pipe_list.extend(create_pipe())


    screen.blit(bg,(0,0))
    if game_active:
        #chim
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(bird,bird_rect)
        game_active= check_collision(pipe_list)
        #ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
    #floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos =0

    pygame.display.update()  
    clock.tick(120)