# Example file showing a circle moving on screen
import pygame, random

# pygame setup

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
dt = 0

sh = screen.get_height()
sw = screen.get_width()

# snk_x = sw / 4
# snk_y = sh / 2
snk_x = 200
snk_y = 400
snake = [
    [snk_x, snk_y],
    [snk_x-20, snk_y],
    [snk_x-40, snk_y]
]

food = [sh/2, sw/2]
isfood  = False

last_key = [
    False,
    False,
    False,
    False
]

while running:
    next_key = pygame.key.get_pressed()
    key = key if next_key == -1 else next_key
    
    
    if snake[0][0] in [0, sw-20] or snake[0][1]  in [0, sh-20]:
        running = False
    
    # or snake[0] in snake[1:]


    new_head = [snake[0][0], snake[0][1]]

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    #generating the background grid
    color = True
    for i in range(0, 800, 20):    
        for j in range(0, 800, 20):
            if color:
                pygame.draw.rect(screen, "grey", (j,i, 20, 20))
            else:
                pygame.draw.rect(screen, "white", (j,i, 20, 20))
            color = not color
        color = not color
        
    if not isfood:
        pygame.draw.rect(screen, "red", (food[0], food[1], 20, 20))



    if (key[pygame.K_w] or last_key[0] == True) and last_key[1] == False:
        new_head[1] -= 20
        last_key = [
            True,
            False,
            False,
            False
        ]

    if (key[pygame.K_s] or last_key[1] == True) and last_key[0] == False:
        new_head[1] += 20
        last_key = [
            False,
            True,
            False,
            False
        ]
    if (key[pygame.K_a] or last_key[2] == True) and last_key[3] == False:
        new_head[0] -= 20
        last_key = [
            False,
            False,
            True,
            False
        ]
    if (key[pygame.K_d] or last_key[3] == True) and last_key[2] == False:
        new_head[0] += 20
        last_key = [
            False,
            False,
            False,
            True
        ]


    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.choice(range(0, sw-1, 20)),
                random.choice(range(0, sh-1, 20))
            ]
            food = nf if nf not in snake else None
        pygame.draw.rect(screen, "red", (food[0], food[1], 20, 20))
    else:
        tail = snake.pop()
        # w.addch(int(tail[0]), int(tail[1]), ' ')
        for i in snake:
            pygame.draw.rect(screen, "green", (i[0], i[1], 20, 20))
    


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(10)

pygame.quit()
