import pygame
import sys

# Algatame Pygame
pygame.init()

# Määrame akna suuruse ja pealkirja
width, height = 300, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lumemees – Karin Eegreid")

# Värvid
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


# Joonistame lumememme
def draw_snowman(surface):
    # Kere
    pygame.draw.circle(surface, white, (150, 220), 60)  # Alumine osa
    pygame.draw.circle(surface, white, (150, 140), 40)  # Keskmine osa
    pygame.draw.circle(surface, white, (150, 100), 30)  # Pea

    # Silmad
    pygame.draw.circle(surface, black, (140, 95), 5)  # Vasak silm
    pygame.draw.circle(surface, black, (160, 95), 5)  # Parem silm

    # Nina
    pygame.draw.circle(surface, red, (150, 105), 5)  # Punane nina

    # Suu
    pygame.draw.arc(surface, black, (130, 90, 40, 20), 3.14 / 2, 2 * 3.14 / 2, 1)  # Kõver suu


# Põhitsükkel
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            # Täidame akna valgega
    window.fill((135, 206, 250))  # Taevasinise värv

    # Joonistame lumememme
    draw_snowman(window)

    # Värskendame ekraani
    pygame.display.update() 