import pygame
import random
from pygame.locals import *

life_continue = [2, 3]
appearance_of_life = [3]


size_of_matrix = 20
size_of_line_in_matrix = 20

width, height = 1000, 1000

rule_change = input('Хотите что-то изменить (задать сид, правила игры, изменить размеры экрана)? \n').lower()
if rule_change == 'y' or rule_change == 'yes' or rule_change == 'да':
    scr = input('Хотите изменить размер экрана (по умолчанию 1000 на 1000)?\n').lower()
    if scr == 'true' or scr == 't' or scr == 'y' or scr == 'yes':
        width = int(input('Введите ширину: '))
        height = int(input('Введите высоту: '))

        screen = pygame.display.set_mode((width, height))
        matrix = [[random.choice([0, 1]) for elem in range(screen.get_width() // size_of_line_in_matrix)] for spis in
                  range(screen.get_height() // size_of_matrix)]

    else:
        screen = pygame.display.set_mode((width, height))
        matrix = [[random.choice([0, 1]) for elem in range(screen.get_width() // size_of_line_in_matrix)] for spis in
                  range(screen.get_height() // size_of_matrix)]

    user = input('Хотите ввести определённую генерацию сида?\n').lower()
    if user == 'y' or user == 'yes' or user == 'да':
        user2 = int(input('Введите целочисленное значение сида: '))
        random.seed(user2)
        matrix = [[random.choice([0, 1]) for elem in range(screen.get_width() // size_of_line_in_matrix)] for spis in range(screen.get_height() // size_of_matrix)]

    rules = input('Хотите изменить правила игры? (изначально если вокруг живой клетки существуют 2 или 3 живые,\nто клетка продолжает жить, если клетка мертва и около неё 3 живые она начнёт жить)\nв ответ принимается true или false: ').lower()
    if rules == 'true' or rules == 't':
        life_cont = int(input('Введите кол-во чисел, которое будет отвечать за причину продолжения жизни: '))
        life_continue = []
        for i in range(life_cont):
            life_continue1 = int(input('Введите причину продолжения жизни (в значениях кол-ва живых клеток вокруг): '))
            life_continue.append(life_continue1)

        app_of_lf = int(input('Введите кол-во чисел, которое будет отвечать за причину появления жизни: '))
        appearance_of_life = []
        for i in range(app_of_lf):
            appearance_of_life1 = int(input('Введите причину появления живой клетки (в значениях кол-ва живых клеток вокруг): '))
            appearance_of_life.append(appearance_of_life1)

else:
    screen = pygame.display.set_mode((width, height))
    matrix = [[random.choice([0, 1]) for elem in range(screen.get_width() // size_of_line_in_matrix)] for spis in
              range(screen.get_height() // size_of_matrix)]

mouse = pygame.mouse.get_pos()

def is_near(matrix_have: list, screen=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
    count = 0
    for i in screen:
        if matrix[(matrix_have[0] + i[0]) % len(matrix)][(matrix_have[1] + i[1]) % len(matrix[0])] == 1:
            count += 1
    return count



print('ПРЕДУПРЕЖДЕНИЕ!!!!! \nМатрица создаётся до начала игры')

print('До начала игры есть кнопки: \ne - стереть матрицу \nr - заново сгенерировать матрицу\nлевая кнопка мыши - поставить клетку \nправая кнопка мыши - убрать клетку\nspase - запустить игру \nПосле начала игры: \ns - остановить игру \nа также выше указанные клавиши')



running = True

while running:

    game_of_life_run = False

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

        for spis in range(0, len(matrix)):
            for elem in range(0, len(matrix[spis])):
                pygame.draw.rect(screen, (0, 255 * matrix[spis][elem], 0), [spis * size_of_matrix, elem * size_of_line_in_matrix, 20, 20])

        if event.type == KEYUP:
            if event.key == K_e:
                for spis in range(0, len(matrix)):
                    for elem in range(0, len(matrix[spis])):
                        matrix[spis][elem] = 0

            if event.key == K_r:
                matrix = [[random.choice([0, 1]) for elem in range(screen.get_width() // size_of_line_in_matrix)] for spis in
                          range(screen.get_height() // size_of_matrix)]

            if event.key == K_SPACE:
                game_of_life_run = True

        if event.type == KEYDOWN:
            if event.key == K_g and event.key == K_d:
                mouse = pygame.mouse.get_pos()
                x = mouse[0] // size_of_line_in_matrix
                y = mouse[1] // size_of_matrix
                for spis in range(0, len(matrix)):
                    for elem in range(0, len(matrix[spis])):
                        if spis == x:
                            if elem == y:
                                matrix[spis - 1][elem] = 1
                                matrix[spis][elem + 1] = 1
                                matrix[spis + 1][elem - 1] = 1
                                matrix[spis + 1][elem] = 1
                                matrix[spis + 1][elem + 1] = 1

        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:
                mouse = pygame.mouse.get_pos()
                x = mouse[0] // size_of_line_in_matrix
                y = mouse[1] // size_of_matrix
                for spis in range(0, len(matrix)):
                    for elem in range(0, len(matrix[spis])):
                        if spis == x:
                            if elem == y:
                                matrix[spis][elem] = 1

            if event.button == 3:
                mouse = pygame.mouse.get_pos()
                x = mouse[0] // size_of_line_in_matrix
                y = mouse[1] // size_of_matrix
                for spis in range(0, len(matrix)):
                    for elem in range(0, len(matrix[spis])):
                        if spis == x:
                            if elem == y:
                                matrix[spis][elem] = 0

            if event.button == 2:
                mouse = pygame.mouse.get_pos()
                x = mouse[0] // size_of_line_in_matrix
                y = mouse[1] // size_of_matrix
                for spis in range(0, len(matrix)):
                    for elem in range(0, len(matrix[spis])):
                        if spis == x:
                            if elem == y:
                                matrix[spis - 1][elem] = 1
                                matrix[spis][elem + 1] = 1
                                matrix[spis + 1][elem - 1] = 1
                                matrix[spis + 1][elem] = 1
                                matrix[spis + 1][elem + 1] = 1




    pygame.display.update()

    while game_of_life_run:

        for event in pygame.event.get():

            if event.type == KEYUP:
                if event.key == K_e:
                    for spis in range(0, len(matrix)):
                        for elem in range(0, len(matrix[spis])):
                            matrix[spis][elem] = 0

                if event.key == K_r:
                    matrix = [[random.choice([0, 1]) for elem in range(screen.get_width() // size_of_line_in_matrix)] for spis in
                              range(screen.get_height() // size_of_matrix)]

                if event.key == K_SPACE:
                    game_of_life_run = True

                if event.key == K_s:
                    game_of_life_run = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    x = mouse[0] // size_of_line_in_matrix
                    y = mouse[1] // size_of_matrix
                    for spis in range(0, len(matrix)):
                        for elem in range(0, len(matrix[spis])):
                            if spis == x:
                                if elem == y:
                                    matrix[spis][elem] = 1

                if event.button == 3:
                    mouse = pygame.mouse.get_pos()
                    x = mouse[0] // size_of_line_in_matrix
                    y = mouse[1] // size_of_matrix
                    for spis in range(0, len(matrix)):
                        for elem in range(0, len(matrix[spis])):
                            if spis == x:
                                if elem == y:
                                    matrix[spis][elem] = 0

                if event.button == 2:
                    mouse = pygame.mouse.get_pos()
                    x = mouse[0] // size_of_line_in_matrix
                    y = mouse[1] // size_of_matrix
                    for spis in range(0, len(matrix)):
                        for elem in range(0, len(matrix[spis])):
                            if spis == x:
                                if elem == y:
                                    matrix[spis - 1][elem] = 1
                                    matrix[spis][elem + 1] = 1
                                    matrix[spis + 1][elem - 1] = 1
                                    matrix[spis + 1][elem] = 1
                                    matrix[spis + 1][elem + 1] = 1

            if event.type == KEYDOWN:
                if event.key == K_g:
                    if event.key == K_d:
                        mouse = pygame.mouse.get_pos()
                        x = mouse[0] // size_of_line_in_matrix
                        y = mouse[1] // size_of_matrix
                        for spis in range(0, len(matrix)):
                            for elem in range(0, len(matrix[spis])):
                                if spis == x:
                                    if elem == y:
                                        matrix[spis - 1][elem] = 1
                                        matrix[spis][elem + 1] = 1
                                        matrix[spis + 1][elem - 1] = 1
                                        matrix[spis + 1][elem] = 1
                                        matrix[spis + 1][elem + 1] = 1

        for spis in range(0, len(matrix)):
            for elem in range(0, len(matrix[spis])):
                pygame.draw.rect(screen, (0, 255 * matrix[spis][elem], 0), [spis * size_of_matrix, elem * size_of_line_in_matrix, 20, 20])

        pygame.display.update()

        matrix2 = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    if is_near([i, j]) not in life_continue:
                        matrix2[i][j] = 0
                        continue
                    matrix2[i][j] = 1
                    continue
                if is_near([i, j]) in appearance_of_life:
                    matrix2[i][j] = 1
                    continue
                matrix2[i][j] = 0
        matrix = matrix2

pygame.quit()