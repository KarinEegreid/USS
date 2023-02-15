# Karl Paju IS22
# Vajalikud packaged
import random

import pygame

# Pygame käivitamine
pygame.init()

# Värvide defineerimine kasutades RGB standardit
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Ekraani loomine ning pealkirja seadistamine
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Karl Paju IS22 Ussimäng')

# Loob mängu kiiruse juhtimiseks kellaobjekt.
clock = pygame.time.Clock()

# Määrame ussi suuruse ning kiiruse
snake_block = 10
snake_speed = 15
# Fontide määramine
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 30)


# Määrab funktsioon Your_score(), et kuvada mängija hetke skoori.
def Your_score(score):
    value = score_font.render("Sinu skoor: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# Määrab funktsioon our_snake(), et joonistada madu ekraanile.
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# Määrab funktsiooni message(), et joonistada ekraanile nõutud värvides teksti.
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# Määrab funktsioon gameLoop(), et käitada mängu seni, kuni mängija kaotab või lahkub.
def gameLoop():
    game_over = False
    game_close = False

    # Mao esialgne asend
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Mao asendi esialgne muutus
    x1_change = 0  # mao esialgne asend x teljel
    y1_change = 0  # mao esialgne asend y teljel

    # Initsialiseerib madu
    snake_List = []
    Length_of_snake = 1

    # Toidu algne asend
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    # Loop kontrollib kas mäng on läbi või ei
    while not game_over:
        # Kui mäng on läbi siis tuleb ekraanile sõnum, et ta kaotas.
        while game_close == True:
            # Display "game over" message
            dis.fill(blue)
            message("Kaotasid. Vajuta C-d, et uuesti mängida või Q-d, et mäng sulgeda.", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Lahkub mängust kui Q-d vajutatakse
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
      
        # nuppude määramine, et uss ekraanil liiguks kasutaja sisestuste järgi.
        for event in pygame.event.get():  # Käib läbi kõik mängus toimunud sündmused
            if event.type == pygame.QUIT:  # Kui kasutaja soovib mängu sulgeda, siis märgib game_over muutuja True'ks
                game_over = True
            if event.type == pygame.KEYDOWN:  # Kui kasutaja vajutab mingit klahvi
                if event.key == pygame.K_LEFT:  # Kui kasutaja vajutab vasakule noolt
                    x1_change = -snake_block  # Muudab mängija x-koordinaati
                    y1_change = 0  # ei muuda y koordinaati
                elif event.key == pygame.K_RIGHT:  # Kui kasutaja vajutab paremale noolt
                    x1_change = snake_block  # muudab mängija x-koordinaati
                    y1_change = 0  # ei muuda y koordinaati
                elif event.key == pygame.K_UP:  # Kui kasutaja vajutab üles noolt
                    y1_change = -snake_block  # Muudab mängija y-koordinaati
                    x1_change = 0  # ei muuda x koordinaati
                elif event.key == pygame.K_DOWN:  # Kui kasutaja vajutab alla noolt
                    y1_change = snake_block  # muudab mängija y-koordinaati
                    x1_change = 0  # ei muuda x koordinaati

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # Kontrollib, kas mängija läheb ekraanist välja
            game_close = True
        x1 += x1_change  # Muudab mängija x-koordinaati vastavalt x1_change väärtusele
        y1 += y1_change  # Muudab mängija y-koordinaati vastavalt y1_change väärtusele
        dis.fill(blue)  # Täidab ekraani sinise värviga
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])  # Joonistab toidu ja määrab selle värvi
        snake_Head = []  # Loob tühja listi mao pea jaoks
        snake_Head.append(x1)  # Lisab x-koordinaadi madala küljega listi
        snake_Head.append(y1)  # Lisab y-koordinaadi madala küljega listi
        snake_List.append(snake_Head)  # Lisab mao pea listi madala küljega
        if len(snake_List) > Length_of_snake:  # Kui madu on pikem kui vaja
            del snake_List[0]  # Eemaldab madu lõpust ühe jupi

        for x in snake_List[:-1]:  # Käib läbi kogu mao
            if x == snake_Head:  # Kui madu põrkab vastu iseennast
                game_close = True  # Mäng lõpetatakse

        our_snake(snake_block, snake_List)  # joonistab ussi
        Your_score(Length_of_snake - 1)  # arvutab skoori lahutades ussi pikkusest ühe

        pygame.display.update()  # uuendab ekraani

        if x1 == foodx and y1 == foody:  # Kui madu sööb toidu
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # Määrab toidu uue x-koordinaadi
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # Määrab toidu uue y-koordinaadi
            Length_of_snake += 1  # Lisab ühe jupi mao pikkusele

        clock.tick(snake_speed)  # Paus mängu kiiruse säilitamiseks

    pygame.quit()  # Sulgeb pygame'i mooduli
    quit()  # Lõpetab programmi töö


gameLoop()

