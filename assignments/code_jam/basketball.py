import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

gradient_surface = pygame.Surface((640, 480))
for y in range(480):
    # Calculate color transition from Red at the top to Blue at the bottom
    # Red goes from 255 down to 0; Blue goes from 0 up to 255
    r = int(238 * (1 - y / 480))
    b = int(75 * (y / 480))
    g = int(43 * (1 - y / 480))
    pygame.draw.line(gradient_surface, (r, g, b), (0, y), (640, y))

my_image = pygame.image.load("assignments/code_jam/media/basketball_small.png")
image_rect = my_image.get_rect(center=(320, 240))



running = True
while running:
    screen.blit(gradient_surface, (0, 0))
    # Image_rect.x += 1 # Move image to the right
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# If image_rect.x > screen.get_width(): # If the image goes off the right edge
# If image_rect.x = -image_rect.width: # Move it to left edge
    screen.blit(my_image, image_rect) 
    pygame.display.flip()
    clock.tick(30) # Limit the frame rate to 60 fps