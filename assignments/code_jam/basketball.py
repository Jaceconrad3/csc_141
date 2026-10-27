# Jace Conrad
# Pygame- Feel the Power!
# Basketball Game
# Runs at 30 fps and allows you to move basketball with arrows
# Can change the speed of basketball by changing the speed variable
# Can change the size of the basketball by changing the image size in the media folder
# Has black backround but you can change it by changing the fill color in the screen.fill code and change numbers
# Difficulty 7/10
# The hardest part was figuring out how to move the basketball with the arrows but I used stack overflow for info. 
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))  # Game window size
clock = pygame.time.Clock() # Controls the frame rate

my_image = pygame.image.load("assignments/code_jam/media/basketball_small.png")
image_rect = my_image.get_rect(center=(400, 400)) # Sets the basketball to the center of the screen 

speed = 10
running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:    # Set it to speed instead of a number so you can change the speed variable.
        image_rect.x -= speed # Moves left by subtracting speed from x-coordinate
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed # Moves right by adding speed to x-coordinate
    if keys[pygame.K_UP]: 
        image_rect.y -= speed # Moves up by subtracting speed from y-coordinate
    if keys[pygame.K_DOWN]:
        image_rect.y += speed # Moves down by adding speed to y-coordinate

    screen.fill((0, 0, 0))  # Makes the screen to black

    screen.blit(my_image, image_rect) 
    
    pygame.display.flip() 
    clock.tick(30)

pygame.quit()