import pygame

# Инициализация Pygame
pygame.init()

# Создание окна (ширина, высота)
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Example")

# # Загрузка изображения  (путь к изображению)
image1 = pygame.image.load("images/pic-python.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("images/pic-pycharm-48.png")
image_rect2 = image2.get_rect()

speed = 1

run = True
while run:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect1.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect1.x += speed
    if keys[pygame.K_UP]:
        image_rect1.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect1.y += speed

# #  For mouse motion
#         if event.type == pygame.MOUSEMOTION:
#            mouse_x, mouse_y = pygame.mouse.get_pos()
#            image_rect.x = mouse_x -24
#            image_rect.y = mouse_y -24


    # Обновление позиции изображения
    # # Отрисовка фона
    screen.fill((0, 0, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()