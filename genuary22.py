import pygame
import sys
import random

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "kitty.jpg"

pygame.display.set_mode((100, 100))

image = pygame.image.load(filename).convert()
screen = pygame.display.set_mode(image.get_size())

class Particle:
    def __init__(self, x, y, c):
        self.pos = pygame.Vector2(x, y)
        self.c = c
        self.r = 1
        self.max_r = random.randint(2, 8)
    
    def update(self, delta):
        self.r = min(self.r + delta * 10, self.max_r)
    
    def draw(self, win):
        pygame.draw.circle(win, self.c, self.pos, self.r)

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

        if not paused:
            spawn_timer -= delta
        if spawn_timer <= 0:
            spawn_timer += time_to_spawn
            time_to_spawn = max(time_to_spawn * 0.75, 0.01)
            x, y = random.randint(0, screen.get_width() - 1), random.randint(0, screen.get_height() - 1)
            color = image.get_at((x, y))
            particles.append(Particle(x, y, color))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    paused = not paused

        for p in particles:
            p.update(delta * 1.25)

        draw(screen, particles)

        pygame.display.flip()

main()