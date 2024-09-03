import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 1200
FPS = 60
NUM_STARS = 200
NUM_CONSTELLATIONS = 5

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")
clock = pygame.time.Clock()

# Pygame Snippet for drawing a circle
def draw_circle(surface, color, pos, radius):
    pygame.draw.circle(surface, color, (int(pos[0]), int(pos[1])), radius)

# Pygame Snippet for drawing a line
def draw_line(surface, color, start_pos, end_pos):
    pygame.draw.line(surface, color, start_pos, end_pos)

# Pygame Snippet for drawing text
def draw_text(surface, text, color, pos, font_size=20):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect(center=(pos[0], pos[1] - font_size))
    surface.blit(text_render, text_rect)

class Planet:
    def __init__(self, name, mass, radius, color, orbital_radius, orbital_speed, moons=None):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color
        self.orbital_radius = orbital_radius
        self.orbital_speed = orbital_speed
        self.angle = 0
        self.moons = moons or []

    def update(self, planets):
       
        self.angle += self.orbital_speed / FPS
        self.x = WIDTH // 2 + self.orbital_radius * math.cos(self.angle)
        self.y = HEIGHT // 2 + self.orbital_radius * math.sin(self.angle)

        # Update moons
        for moon in self.moons:
            moon.update(self)

    def draw(self):
        draw_circle(screen, self.color, (self.x, self.y), self.radius)
        draw_line(screen, (255, 255, 255), (WIDTH // 2, HEIGHT // 2), (self.x, self.y))

        # Draw planet name
        draw_text(screen, self.name, (255, 255, 255), (self.x, self.y), font_size=15)

        # Draw moons
        for moon in self.moons:
            moon.draw()

class Moon:
    def __init__(self, name, radius, color, orbital_radius, orbital_speed):
        self.name = name
        self.radius = radius
        self.color = color
        self.orbital_radius = orbital_radius
        self.orbital_speed = orbital_speed
        self.angle = 0

    def update(self, planet):
       
        self.angle += self.orbital_speed / FPS
        self.x = planet.x + self.orbital_radius * math.cos(self.angle)
        self.y = planet.y + self.orbital_radius * math.sin(self.angle)

    def draw(self):
        draw_circle(screen, self.color, (self.x, self.y), self.radius)

# Create planets
sun = Planet("Sun", 1989000, 50, (255, 255, 0), 0, 0)

mercury = Planet("Mercury", 0.330, 5, (169, 169, 169), 70, 2 * math.pi / 90)
venus = Planet("Venus", 4.87, 10, (255, 165, 0), 110, 2 * math.pi / 225)
earth = Planet("Earth", 5.97, 20, (0, 0, 255), 150, 2 * math.pi / 365)
mars = Planet("Mars", 0.641, 8, (255, 0, 0), 220, 2 * math.pi / 687)
jupiter = Planet("Jupiter", 1898, 30, (255, 165, 0), 350, 2 * math.pi / (12 * 365))
saturn = Planet("Saturn", 568, 25, (255, 255, 0), 480, 2 * math.pi / (29.5 * 365))
uranus = Planet("Uranus", 86.8, 20, (0, 255, 0), 600, 2 * math.pi / (84 * 365))
neptune = Planet("Neptune", 102, 18, (0, 0, 255), 730, 2 * math.pi / (165 * 365))

# Create moons
moon_earth_1 = Moon("Moon", 8, (200, 200, 200), 50, 2 * math.pi / 30)
moon_mars_1 = Moon("Phobos", 4, (200, 200, 200), 30, 2 * math.pi / 0.32)
moon_mars_2 = Moon("Deimos", 3, (200, 200, 200), 40, 2 * math.pi / 1.2)
moon_jupiter_1 = Moon("Io", 10, (200, 200, 200), 80, 2 * math.pi / 1.7)
moon_jupiter_2 = Moon("Europa", 8, (200, 200, 200), 100, 2 * math.pi / 3)
moon_jupiter_3 = Moon("Ganymede", 12, (200, 200, 200), 130, 2 * math.pi / 5)
moon_jupiter_4 = Moon("Callisto", 11, (200, 200, 200), 160, 2 * math.pi / 7)

earth.moons.extend([moon_earth_1])
mars.moons.extend([moon_mars_1, moon_mars_2])
jupiter.moons.extend([moon_jupiter_1, moon_jupiter_2, moon_jupiter_3, moon_jupiter_4])

planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Generate stars 
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update planets
    for planet in planets:
        planet.update(planets)

    # Draw background with stars
    screen.fill((0, 0, 0))
    for star in stars:
        draw_circle(screen, (255, 255, 255), star, 1)

    # Draw planets and moons
    for planet in planets:
        planet.draw()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
