# Karl Paju IS22
# Vajalikud packaged
import random

import pygame

# Pygame käivitamine
pygame.init()

# Värvide defineerimine kasutades RGB standardit
white = (255, 255, 255)  # valge värv
yellow = (255, 255, 102)  # kollane värv
black = (0, 0, 0)  # must värv
red = (213, 50, 80)  # punane värv
green = (0, 255, 0)  # roheline värv
blue = (50, 153, 213)  # sinine värv

# Ekraani loomine ning pealkirja seadistamine
dis_width = 800  # ekraani laius
dis_height = 600  # ekraani pikkus

dis = pygame.display.set_mode((dis_width, dis_height))  # loob ekraani
pygame.display.set_caption('Karl Paju IS22 Ussimäng')  # loob ekraani nime

# Loob mängu kiiruse juhtimiseks kellaobjekt.
clock = pygame.time.Clock()

# Määrame ussi suuruse ning kiiruse
snake_block = 10  # Määrab iga mao osa suuruse, mis on 10 pikslit.
snake_speed = 15  # Määrab mao liikumiskiiruse pikslites sekundis.

# Fontide määramine
font_style = pygame.font.SysFont("bahnschrift", 20)  # loob tavalise fonti mida saab kasutada nt death screeni loomisel
score_font = pygame.font.SysFont("comicsansms", 30)  # loob skoori fonti


# Määrab funktsioon Your_score(), et kuvada mängija hetke skoori.
def Your_score(score):  # Funktsioon kuvab mängija skoori mängu ekraani ülemises vasakus nurgas.
    value = score_font.render("Sinu skoor: " + str(score), True,
                              yellow)  # Renderdab skoori sõne vastavalt fondile ja salvestab selle muutujasse value.
    dis.blit(value, [0, 0])  # Kuvab skoori muutuja value väärtuse mängu akna ülemises vasakus nurgas.


# Määrab funktsioon our_snake(), et joonistada madu ekraanile.
def our_snake(snake_block, snake_list):  # Funktsioon joonistab kogu ussi tema iga elemendi abil.
    for x in snake_list:
        # Joonistab iga ussi elemendi abil uue musta ristküliku pygame'i abil.
        # x[0] ja x[1] on koordinaadid, kus antud elemendiga ristkülik joonistatakse.
        # x[0] ja x[1] vastavad ussi elemendi x- ja y-koordinaatidele.
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# Määrab funktsiooni message(), et joonistada ekraanile nõutud värvides teksti.
def message(msg, color):  # Funktsioon kuvab sõnumi mängu ekraanil.
    mesg = font_style.render(msg, True, color)  # Teksti renderdamine spetsiaalse fondiga ja värvi andmine
    dis.blit(mesg, [dis_width / 6, dis_height / 3])  # Teksti kuvamine ekraanil


# Määrab funktsioon gameLoop(), et käitada mängu seni, kuni mängija kaotab või lahkub.
def gameLoop():
    game_over = False
    game_close = False

    # Mao esialgne asend
    x1 = dis_width / 2  # mao esialgne asend paigutatakse keskele x teljes jagades ekraani laiust kahega
    y1 = dis_height / 2  # mao esialgne asend paigutatakse keskele y teljes jagades ekraani pikkust kahega

    # Mao asendi esialgne muutus
    x1_change = 0  # mao esialgne asend x teljel
    y1_change = 0  # mao esialgne asend y teljel

    # Initsialiseerib madu
    snake_List = []  # Loob mängija "mao" listi, mida kasutatakse mao keha hoidmiseks
    Length_of_snake = 1  # Määrab mao algse pikkuse üheks, kuna see koosneb ainult pea osast

    # Toidu algne asend
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # paigutab ussi toidu x teljele
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # paigutab ussi toidu y teljele
    # Loop kontrollib kas mäng on läbi või ei
    while not game_over:  # T # Tsükkel, mis käivitub seni kuni mäng pole läbi
        # Kui mäng on läbi, siis kuvatakse ekraanile sõnum, mis ütleb, et mängija kaotas
        while game_close == True:  # Sisemine tsükkel, mis käivitub, kui mängija kaotas

            dis.fill(blue)  # Tühjendab ekraani sinise värviga
            message("Kaotasid. Vajuta C-d, et uuesti mängida või Q-d, et mäng sulgeda.",
                    red)  # Kutsub esile funktsiooni message, mis kuvab ekraanile teate
            Your_score(Length_of_snake - 1)  # arvutab skoori lahutades ära number ühe ussi pikkusest
            pygame.display.update()  # uuendab ekraani

            for event in pygame.event.get():  # Tsükkel sündmuste jaoks, mis käivitatakse, kui kasutaja midagi teeb
                if event.type == pygame.KEYDOWN:  # Kui kasutaja vajutab klahvi
                    if event.key == pygame.K_q:  # Kui kasutaja vajutab Q klahvi
                        game_over = True  # Lõpeta mäng
                        game_close = False  # Ära lase ekraanile teksti väljastada
                    if event.key == pygame.K_c:  # Kui kasutaja vajutab C klahvi
                        gameLoop()  # Käivita uus mäng, kutsudes funktsiooni gameLoop()

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

