import pygame
import sys
import random

# Choose filename
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "kitty.jpg"

# Initialize the screen with the image
pygame.display.set_mode((100, 100))

image = pygame.image.load(filename).convert()
screen = pygame.display.set_mode(image.get_size())

# Class for the circles that make up the image
class Particle:
    def __init__(self, x, y, c):
        self.pos = pygame.Vector2(x, y)
        self.c = c
        self.r = 1
        self.max_r = random.randint(2, 8)

    # Add to the radius and clamp
    def update(self, delta):
        self.r = min(self.r + delta * 10, self.max_r)
    
    def draw(self, win):
        pygame.draw.circle(win, self.c, self.pos, self.r)

# Draw all the particles
def draw(win, particles):
    win.fill("black")
    # win.blit(image, (0, 0))

    for p in particles:
        p.draw(win)

def main():
    pygame.time.delay(1)
    delta = pt = 0
    particles = []
    spawn_timer = 1
    time_to_spawn = 1
    paused = True
    run = True
    while run:
        ticks = pygame.time.get_ticks()
        delta = (ticks - pt) / 1000
        pt = ticks

        # As long as not paused, update the particle spawn timer
        if not paused:
            spawn_timer -= delta
        if spawn_timer <= 0:
            # Make each particle take less time to spawn
            spawn_timer += time_to_spawn
            time_to_spawn = max(time_to_spawn * 0.75, 0.01)
            # Get a random position to put the particle
            x, y = random.randint(0, screen.get_width() - 1), random.randint(0, screen.get_height() - 1)
            # Find the RGB color at that position
            color = image.get_at((x, y))
            # Make new particle
            particles.append(Particle(x, y, color))

        # Event loop for closing window and pausing
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    paused = not paused

        # Update particles
        for p in particles:
            p.update(delta * 1.25)

        draw(screen, particles)

        # Show what's on the screen
        pygame.display.flip()

# Run all the stuff
main()
