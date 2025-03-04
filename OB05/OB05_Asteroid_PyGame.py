import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
SHIP_SIZE = 50
ASTEROID_SIZE = 50
BULLET_SIZE = 5
SHIP_SPEED = 3
ASTEROID_SPEED = 2
BULLET_SPEED = 7
MAX_LIVES = 4

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космическая игра")

# Загрузка изображений
ship_image = pygame.Surface((SHIP_SIZE, SHIP_SIZE))
ship_image.fill(WHITE)
ship_image = pygame.image.load('images/rocketship.png')  # Загрузка изображения корабля
ship_image = pygame.transform.scale(ship_image, (SHIP_SIZE, SHIP_SIZE))  # Изменение размера изображения корабля

asteroid_images = [
    pygame.image.load('images/asteroid.png'),
    pygame.image.load('images/meteorite.png'),
    pygame.image.load('images/starfish.png'),
    pygame.image.load('images/stone.png')
]
asteroid_images = [pygame.transform.scale(img, (ASTEROID_SIZE, ASTEROID_SIZE)) for img in asteroid_images]

# asteroid_image = pygame.Surface((ASTEROID_SIZE, ASTEROID_SIZE))
# asteroid_image.fill(RED)
# asteroid_image = pygame.image.load('asteroid.png')  # Загрузка изображения астероидов
# asteroid_image = pygame.transform.scale(asteroid_image, (ASTEROID_SIZE, ASTEROID_SIZE))  # Изменение размера изображения астероидов

# Звуки
shoot_sound = pygame.mixer.Sound('sounds/laser-blip.wav')  # Звук выстрела
explode_sound = pygame.mixer.Sound('sounds/explosion.wav')  # Звук взрыва

# Класс корабля
class Ship:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - SHIP_SIZE - 10, SHIP_SIZE, SHIP_SIZE)
        self.lives = MAX_LIVES

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(WIDTH - SHIP_SIZE, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - SHIP_SIZE, self.rect.y))

    def draw(self):
        screen.blit(ship_image, self.rect.topleft)

# Класс астероида
class Asteroid:
    def __init__(self):
        self.image = random.choice(asteroid_images)
        self.rect = pygame.Rect(random.randint(0, WIDTH - ASTEROID_SIZE), 0, ASTEROID_SIZE, ASTEROID_SIZE)
    def move(self):
        self.rect.y += ASTEROID_SPEED
    def draw(self):
        screen.blit(self.image, self.rect.topleft)

# Класс пули
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_SIZE, BULLET_SIZE)
    def move(self):
        self.rect.y -= BULLET_SPEED
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    ship = Ship()
    asteroids = []
    score = 0
    bullets = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Управление кораблем
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ship.move(-SHIP_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            ship.move(SHIP_SPEED, 0)
        if keys[pygame.K_UP]:
            ship.move(0, -SHIP_SPEED)
        if keys[pygame.K_DOWN]:
            ship.move(0, SHIP_SPEED)
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:  # Ограничение на количество пуль
                bullets.append(Bullet(ship.rect.centerx, ship.rect.top))
                shoot_sound.play()  # Воспроизведение звука выстрела
 # Создание новых астероидов
        if random.randint(1, 30) == 1:
            asteroids.append(Asteroid())

        # Обновление положения астероидов и пуль
        for asteroid in asteroids[:]:
            asteroid.move()
            if asteroid.rect.top > HEIGHT:
                asteroids.remove(asteroid)

        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        # Проверка на столкновения
        for asteroid in asteroids[:]:
            for bullet in bullets[:]:
                if asteroid.rect.colliderect(bullet.rect):
                    asteroids.remove(asteroid)
                    bullets.remove(bullet)
                    explode_sound.play()
                    score += 1
                    break

            if asteroid.rect.colliderect(ship.rect):
                asteroids.remove(asteroid)
                ship.lives -= 1
                if ship.lives <= 0:
                    running = False

        # Отрисовка
        screen.fill(BLACK)
        ship.draw()
        for asteroid in asteroids:
            asteroid.draw()
        for bullet in bullets:
            bullet.draw()

        # Отображение жизней
        font = pygame.font.SysFont(None, 36)
        lives_text = font.render(f'Lives: {ship.lives}', True, WHITE)
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(lives_text, (10, 10))
        screen.blit(score_text, (10, 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()