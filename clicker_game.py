import pygame
import random

pygame.init()


screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Кликер")


WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont(None, 55)


button_width = 200
button_height = 100
button_x = random.randint(0, screen_width - button_width)
button_y = random.randint(0, screen_height - button_height)


score = 0
clock = pygame.time.Clock()

def draw_button():
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))

def draw_score():
    score_text = font.render(f"Очки: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

running = True
while running:
    screen.fill((0, 0, 0))

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                score += 1
                button_x = random.randint(0, screen_width - button_width)
                button_y = random.randint(0, screen_height - button_height)

    
    draw_button()
    draw_score()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
