import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Fireworks Display")

# Colors
BLACK = (0, 0, 0)

# Particle class for firework sparks
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(2, 4)
        self.speed = random.uniform(2, 6)
        self.angle = random.uniform(0, 2 * math.pi)
        self.lifetime = random.randint(30, 60)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.lifetime -= 1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Firework class
class Firework:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT // 2)
        self.color = random.choice([
            (255, 0, 0),  # Red
            (0, 255, 0),  # Green
            (0, 0, 255),  # Blue
            (255, 255, 0),  # Yellow
            (255, 0, 255),  # Magenta
            (0, 255, 255)  # Cyan
        ])
        self.particles = [Particle(self.x, self.y, self.color) for _ in range(50)]

    def explode(self, surface):
        for particle in self.particles[:]:
            particle.move()
            particle.draw(surface)
            if particle.lifetime <= 0:
                self.particles.remove(particle)

# Main loop
def main():
    clock = pygame.time.Clock()
    fireworks = []
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Add new fireworks at random intervals
        if random.random() < 0.02:  # Adjust for frequency
            fireworks.append(Firework())

        # Update and draw all fireworks
        for firework in fireworks[:]:
            firework.explode(screen)
            if not firework.particles:
                fireworks.remove(firework)

        # Refresh the screen
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
