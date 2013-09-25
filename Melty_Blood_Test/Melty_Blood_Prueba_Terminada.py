import pygame
from pygame import time as pytime
from pygame.locals import *
import time
import sys

screen_w = 640
screen_h = 480

def main():
    pygame.mixer.init()
    pygame.mixer.music.load("melty_blood_song.mp3")
    pygame.mixer.music.play(-1)

    pygame.init()# este comando inicia la aplicacion    
    screen = pygame.display.set_mode((screen_w, screen_h),FULLSCREEN) # comando para desplegar fondo
    pygame.display.set_caption("Melty Blood 2.0") # comando para desplegar mensaje en la ventana
    
    fondo = pygame.image.load("stage.jpg").convert()
    x = 80
    y = 20
    i = 8
    v = 0 # frames animacion
    u = 0 # frames agacharse, saltar, golpear
    time = 100 # stand by
    time_2 = 70 # movimiento
    time_3 = 35 # agacharse
    time_4 = 0 # espera de agacharse
    estado = 0
    pos = 0
    final_1 = 85
    final_2 = 10
           
    Akiha_00 = {} # stand by derecha 
    Akiha_00[0]=("aki00_000.png")
    Akiha_00[1]=("aki00_001.png")
    Akiha_00[2]=("aki00_002.png")
    Akiha_00[3]=("aki00_003.png")
    Akiha_00[4]=("aki00_004.png")
    Akiha_00[5]=("aki00_005.png")
    Akiha_00[6]=("aki00_006.png")
    Akiha_00[7]=("aki00_007.png")
    Akiha_00[8]=("aki00_008.png")
    Akiha_00[9]=("aki00_009.png")
    Akiha_00[10]=("aki00_010.png")
    Akiha_00[11]=("aki00_011.png")

    Akihar_00 = {} # stand by izquierda
    Akihar_00[0]=("aki00r_000.png")
    Akihar_00[1]=("aki00r_001.png")
    Akihar_00[2]=("aki00r_002.png")
    Akihar_00[3]=("aki00r_003.png")
    Akihar_00[4]=("aki00r_004.png")
    Akihar_00[5]=("aki00r_005.png")
    Akihar_00[6]=("aki00r_006.png")
    Akihar_00[7]=("aki00r_007.png")
    Akihar_00[8]=("aki00r_008.png")
    Akihar_00[9]=("aki00r_009.png")
    Akihar_00[10]=("aki00r_010.png")
    Akihar_00[11]=("aki00r_011.png")
            
    Akiha_01 = {} # animacion caminar derecha
    Akiha_01[0]=("aki26_000.png")
    Akiha_01[1]=("aki26_001.png")
    Akiha_01[2]=("aki26_002.png")
    Akiha_01[3]=("aki26_003.png")
    Akiha_01[4]=("aki26_004.png")
    Akiha_01[5]=("aki26_005.png")
    Akiha_01[6]=("aki26_006.png")
    Akiha_01[7]=("aki26_007.png")
    Akiha_01[8]=("aki26_008.png")
    Akiha_01[9]=("aki26_009.png")
    Akiha_01[10]=("aki26_010.png")
    Akiha_01[11]=("aki26_010.png")
    Akiha_01[12]=("aki26_011.png")
    Akiha_01[13]=("aki26_012.png")

    Akihar_01 = {} # animacion caminar izquierda
    Akihar_01[0]=("aki26r_000.png")
    Akihar_01[1]=("aki26r_001.png")
    Akihar_01[2]=("aki26r_002.png")
    Akihar_01[3]=("aki26r_003.png")
    Akihar_01[4]=("aki26r_004.png")
    Akihar_01[5]=("aki26r_005.png")
    Akihar_01[6]=("aki26r_006.png")
    Akihar_01[7]=("aki26r_007.png")
    Akihar_01[8]=("aki26r_008.png")
    Akihar_01[9]=("aki26r_009.png")
    Akihar_01[10]=("aki26r_010.png")
    Akihar_01[11]=("aki26r_010.png")
    Akihar_01[12]=("aki26r_011.png")
    Akihar_01[13]=("aki26r_012.png")

    Akiha_02 = {} # animacion abajo derecha
    Akiha_02[0]=("aki28_000.png")
    Akiha_02[1]=("aki28_001.png")
    Akiha_02[2]=("aki28_002.png")
    Akiha_02[3]=("aki28_003.png")
    Akiha_02[4]=("aki28_004.png")
    Akiha_02[5]=("aki28_005.png")
    Akiha_02[6]=("aki28_006.png")
    Akiha_02[7]=("aki28_007.png")
    Akiha_02[8]=("aki28_008.png")
    Akiha_02[9]=("aki28_009.png")
    Akiha_02[10]=("aki28_010.png")
    Akiha_02[11]=("aki28_011.png")
    Akiha_02[12]=("aki28_012.png")
    Akiha_02[13]=("aki28_013.png")

    Akihar_02 = {} # animacion abajo derecha
    Akihar_02[0]=("aki28r_000.png")
    Akihar_02[1]=("aki28r_001.png")
    Akihar_02[2]=("aki28r_002.png")
    Akihar_02[3]=("aki28r_003.png")
    Akihar_02[4]=("aki28r_004.png")
    Akihar_02[5]=("aki28r_005.png")
    Akihar_02[6]=("aki28r_006.png")
    Akihar_02[7]=("aki28r_007.png")
    Akihar_02[8]=("aki28r_008.png")
    Akihar_02[9]=("aki28r_009.png")
    Akihar_02[10]=("aki28r_010.png")
    Akihar_02[11]=("aki28r_011.png")
    Akihar_02[12]=("aki28r_012.png")
    Akihar_02[13]=("aki28r_013.png")

    Akiha_03 = {} # animacion hacia arriba derecha
    Akiha_03[0]=("aki17_000.png")
    Akiha_03[1]=("aki17_001.png")
    Akiha_03[2]=("aki17_002.png")
    Akiha_03[3]=("aki17_003.png")
    Akiha_03[4]=("aki17_004.png")
    Akiha_03[5]=("aki17_005.png")
    Akiha_03[6]=("aki17_006.png")
    Akiha_03[7]=("aki17_007.png")
    Akiha_03[8]=("aki17_008.png")
    Akiha_03[9]=("aki17_009.png")
    Akiha_03[10]=("aki17_010.png")
    Akiha_03[11]=("aki17_011.png")
    Akiha_03[12]=("aki17_012.png")
    Akiha_03[13]=("aki17_013.png")
    Akiha_03[14]=("aki17_014.png")
    Akiha_03[15]=("aki17_015.png")
    Akiha_03[16]=("aki17_016.png")
    Akiha_03[17]=("aki17_017.png")
    Akiha_03[18]=("aki17_018.png")
    Akiha_03[19]=("aki17_019.png")
    Akiha_03[20]=("aki17_020.png")
    Akiha_03[21]=("aki17_021.png")
    Akiha_03[22]=("aki17_022.png")
    Akiha_03[23]=("aki17_023.png")
    Akiha_03[24]=("aki17_024.png")
    Akiha_03[25]=("aki17_025.png")
    Akiha_03[26]=("aki17_026.png")
    Akiha_03[27]=("aki17_027.png")

    Akihar_03 = {} # animacion hacia arriba izquierda
    Akihar_03[0]=("aki17r_000.png")
    Akihar_03[1]=("aki17r_001.png")
    Akihar_03[2]=("aki17r_002.png")
    Akihar_03[3]=("aki17r_003.png")
    Akihar_03[4]=("aki17r_004.png")
    Akihar_03[5]=("aki17r_005.png")
    Akihar_03[6]=("aki17r_006.png")
    Akihar_03[7]=("aki17r_007.png")
    Akihar_03[8]=("aki17r_008.png")
    Akihar_03[9]=("aki17r_009.png")
    Akihar_03[10]=("aki17r_010.png")
    Akihar_03[11]=("aki17r_011.png")
    Akihar_03[12]=("aki17r_012.png")
    Akihar_03[13]=("aki17r_013.png")
    Akihar_03[14]=("aki17r_014.png")
    Akihar_03[15]=("aki17r_015.png")
    Akihar_03[16]=("aki17r_016.png")
    Akihar_03[17]=("aki17r_017.png")
    Akihar_03[18]=("aki17r_018.png")
    Akihar_03[19]=("aki17r_019.png")
    Akihar_03[20]=("aki17r_020.png")
    Akihar_03[21]=("aki17r_021.png")
    Akihar_03[22]=("aki17r_022.png")
    Akihar_03[23]=("aki17r_023.png")
    Akihar_03[24]=("aki17r_024.png")
    Akihar_03[25]=("aki17r_025.png")
    Akihar_03[26]=("aki17r_026.png")
    Akihar_03[27]=("aki17r_027.png")

    Akiha_04 = {} # light punch derecha
    Akiha_04[0]=("aki01_000.png")
    Akiha_04[1]=("aki01_001.png")
    Akiha_04[2]=("aki01_002.png")
    Akiha_04[3]=("aki01_003.png")
    Akiha_04[4]=("aki01_004.png")
    Akiha_04[5]=("aki01_005.png")
    
    Akihar_04 = {} # light punch izquierda
    Akihar_04[0]=("aki01r_000.png")
    Akihar_04[1]=("aki01r_001.png")
    Akihar_04[2]=("aki01r_002.png")
    Akihar_04[3]=("aki01r_003.png")
    Akihar_04[4]=("aki01r_004.png")
    Akihar_04[5]=("aki01r_005.png")

    Akiha_05 = {} # media punch derecha
    Akiha_05[0]=("aki38_000.png")
    Akiha_05[1]=("aki38_001.png")
    Akiha_05[2]=("aki38_002.png")
    Akiha_05[3]=("aki38_003.png")
    Akiha_05[4]=("aki38_004.png")
    Akiha_05[5]=("aki38_005.png")

    Akihar_05 = {} # media punch izquierda
    Akihar_05[0]=("aki38r_000.png")
    Akihar_05[1]=("aki38r_001.png")
    Akihar_05[2]=("aki38r_002.png")
    Akihar_05[3]=("aki38r_003.png")
    Akihar_05[4]=("aki38r_004.png")
    Akihar_05[5]=("aki38r_005.png")

    Akiha_06 = {} # high kick derecha 
    Akiha_06[0]=("aki40_000.png")
    Akiha_06[1]=("aki40_001.png")
    Akiha_06[2]=("aki40_002.png")
    Akiha_06[3]=("aki40_003.png")
    Akiha_06[4]=("aki40_004.png")
    Akiha_06[5]=("aki40_005.png")
    Akiha_06[6]=("aki40_006.png")
    Akiha_06[7]=("aki40_007.png")
    Akiha_06[8]=("aki40_008.png")
    Akiha_06[9]=("aki40_009.png")
    Akiha_06[10]=("aki40_010.png")

    Akihar_06 = {} # high kick izquierda 
    Akihar_06[0]=("aki40r_000.png")
    Akihar_06[1]=("aki40r_001.png")
    Akihar_06[2]=("aki40r_002.png")
    Akihar_06[3]=("aki40r_003.png")
    Akihar_06[4]=("aki40r_004.png")
    Akihar_06[5]=("aki40r_005.png")
    Akihar_06[6]=("aki40r_006.png")
    Akihar_06[7]=("aki40r_007.png")
    Akihar_06[8]=("aki40r_008.png")
    Akihar_06[9]=("aki40r_009.png")
    Akihar_06[10]=("aki40r_010.png")

    Akiha_07 = {} # animacion saltar arriba derecha
    Akiha_07[0]=("aki15_000.png")
    Akiha_07[1]=("aki15_001.png")
    Akiha_07[2]=("aki15_002.png")
    Akiha_07[3]=("aki15_003.png")
    Akiha_07[4]=("aki15_004.png")
    Akiha_07[5]=("aki15_005.png")
    Akiha_07[6]=("aki15_006.png")
    Akiha_07[7]=("aki15_007.png")
    Akiha_07[8]=("aki15_008.png")
    Akiha_07[9]=("aki15_009.png")
    Akiha_07[10]=("aki15_010.png")
    Akiha_07[11]=("aki15_011.png")
    Akiha_07[12]=("aki15_012.png")
    Akiha_07[13]=("aki15_013.png")
    Akiha_07[14]=("aki15_014.png")
    Akiha_07[15]=("aki15_015.png")
    Akiha_07[16]=("aki15_016.png")
    Akiha_07[17]=("aki15_017.png")
    Akiha_07[18]=("aki15_018.png")
    Akiha_07[19]=("aki15_019.png")
    Akiha_07[20]=("aki15_020.png")
    Akiha_07[21]=("aki15_021.png")
    Akiha_07[22]=("aki15_022.png")
    Akiha_07[23]=("aki15_023.png")

    Akihar_07 = {} # animacion saltar arriba izquierda
    Akihar_07[0]=("aki15r_000.png")
    Akihar_07[1]=("aki15r_001.png")
    Akihar_07[2]=("aki15r_002.png")
    Akihar_07[3]=("aki15r_003.png")
    Akihar_07[4]=("aki15r_004.png")
    Akihar_07[5]=("aki15r_005.png")
    Akihar_07[6]=("aki15r_006.png")
    Akihar_07[7]=("aki15r_007.png")
    Akihar_07[8]=("aki15r_008.png")
    Akihar_07[9]=("aki15r_009.png")
    Akihar_07[10]=("aki15r_010.png")
    Akihar_07[11]=("aki15r_011.png")
    Akihar_07[12]=("aki15r_012.png")
    Akihar_07[13]=("aki15r_013.png")
    Akihar_07[14]=("aki15r_014.png")
    Akihar_07[15]=("aki15r_015.png")
    Akihar_07[16]=("aki15r_016.png")
    Akihar_07[17]=("aki15r_017.png")
    Akihar_07[18]=("aki15r_018.png")
    Akihar_07[19]=("aki15r_019.png")
    Akihar_07[20]=("aki15r_020.png")
    Akihar_07[21]=("aki15r_021.png")
    Akihar_07[22]=("aki15r_022.png")
    Akihar_07[23]=("aki15r_023.png")

    Akiha_08 = {} # animacion burla derecha
    Akiha_08[0]=("aki93_000.png")
    Akiha_08[1]=("aki93_001.png")
    Akiha_08[2]=("aki93_002.png")
    Akiha_08[3]=("aki93_003.png")
    Akiha_08[4]=("aki93_004.png")
    Akiha_08[5]=("aki93_005.png")
    Akiha_08[6]=("aki93_006.png")
    Akiha_08[7]=("aki93_007.png")
    Akiha_08[8]=("aki93_008.png")
    Akiha_08[9]=("aki93_009.png")
    Akiha_08[10]=("aki93_010.png")
    Akiha_08[11]=("aki93_011.png")
    Akiha_08[12]=("aki93_012.png")
    Akiha_08[13]=("aki93_013.png")

    Akihar_08 = {} # animacion burla derecha
    Akihar_08[0]=("aki93r_000.png")
    Akihar_08[1]=("aki93r_001.png")
    Akihar_08[2]=("aki93r_002.png")
    Akihar_08[3]=("aki93r_003.png")
    Akihar_08[4]=("aki93r_004.png")
    Akihar_08[5]=("aki93r_005.png")
    Akihar_08[6]=("aki93r_006.png")
    Akihar_08[7]=("aki93r_007.png")
    Akihar_08[8]=("aki93r_008.png")
    Akihar_08[9]=("aki93r_009.png")
    Akihar_08[10]=("aki93r_010.png")
    Akihar_08[11]=("aki93r_011.png")
    Akihar_08[12]=("aki93r_012.png")
    Akihar_08[13]=("aki93r_013.png")

    while True:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
               if pygame.key.get_pressed()[K_RIGHT]:
                    estado = 1
                    pos = 0
                    if pygame.key.get_pressed()[K_UP]:
                        u = 0
                        estado = 9 # salto hacia derecha
                                                           
               elif pygame.key.get_pressed()[K_LEFT]:
                    estado = 2
                    pos = 1
                    if pygame.key.get_pressed()[K_UP]:
                        u = 0
                        estado = 9 # salto hacia izquierda

               elif pygame.key.get_pressed()[K_DOWN]:
                   estado = 3 # agacharse
                   if pygame.key.get_pressed()[K_a]: #golpe bajo
                       u = 0
                       estado = 11
           
               elif pygame.key.get_pressed()[K_UP]:
                    u = 0
                    estado = 5 # saltar hacia arriba
                                        
               elif pygame.key.get_pressed()[K_a]:
                    u = 0
                    estado = 6 # light punch

               elif pygame.key.get_pressed()[K_s]:
                    u = 0
                    estado = 7 # media punch  

               elif pygame.key.get_pressed()[K_d]:
                    u = 0
                    estado = 8 # high kick

               elif pygame.key.get_pressed()[K_g]:
                    u = 0
                    estado = 10 # burla

                                  
               if pygame.key.get_pressed()[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                   
            elif event.type == KEYUP:
               if estado == 3:
                    v = 0
                    estado = 4 # levantarse
               else:
                    v = 0
                    estado = 0
               
                   
               
               
        if estado == 0 and pos == 0: # stand by derecha
            u = 0
            if v <= 11:
                akiha = pygame.image.load(Akiha_00[v]).convert_alpha()
                screen.blit(fondo,(0,0))
                screen.blit(akiha, (x, y))
                pygame.display.flip()
                pygame.time.wait(time)
                v += 1
                if v > 11:
                    v = 0

        if estado == 0 and pos == 1: # stand by izquierda
             u = 0
             if v <= 11:
                akiha = pygame.image.load(Akihar_00[v]).convert_alpha()
                screen.blit(fondo,(0,0))
                screen.blit(akiha, (x, y))
                pygame.display.flip()
                pygame.time.wait(time)
                v += 1
                if v > 11:
                    v = 0
           
        elif estado == 1: # caminar derecha
            u = 0
            akiha = pygame.image.load(Akiha_01[v]).convert_alpha()
            screen.blit(fondo,(0,0))
            screen.blit(akiha, (x, y))
            pygame.display.flip()
            pygame.time.wait(time_2)
            x += i
            v += 1
            if v > 13:
                v = 1
                
        elif estado == 2: # caminar izquierda
            u = 0
            akiha = pygame.image.load(Akihar_01[v]).convert_alpha()
            screen.blit(fondo,(0,0))
            screen.blit(akiha, (x, y))
            pygame.display.flip()
            pygame.time.wait(time_2)
            x -= i
            v += 1
            if v > 13:
                v = 1

        elif estado == 3 and pos == 0: # agacharse a la derecha
            if u < 5:
                akiha = pygame.image.load(Akiha_02[u]).convert_alpha()
                screen.blit(fondo,(0,0))
                screen.blit(akiha, (x, y))
                pygame.display.flip()
                pygame.time.wait(time_3)
                u += 1

            if u == 5:
                akiha = pygame.image.load(Akiha_02[u]).convert_alpha()
                screen.blit(fondo,(0,0))
                screen.blit(akiha, (x, y))
                pygame.display.flip()
                
                

                
        elif estado == 3 and pos == 1: # agacharse a la izquierda
            if u < 5:
                akiha = pygame.image.load(Akihar_02[u]).convert_alpha()
                screen.blit(fondo,(0,0))
                screen.blit(akiha, (x, y))
                pygame.display.flip()
                pygame.time.wait(time_3)
                u += 1
                

            if u == 5:
                akiha = pygame.image.load(Akihar_02[u]).convert_alpha()
                screen.blit(fondo,(0,0))
                screen.blit(akiha, (x, y))
                pygame.display.flip()
                
                    
                


        elif estado == 4 and pos == 0: # levantarse a la derecha
            if u < 14:
                akiha = pygame.image.load(Akiha_02[u]).convert_alpha()
                screen.blit(fondo,(0,0))
                screen.blit(akiha, (x, y))
                pygame.display.flip()
                pygame.time.wait(time_3)
                u += 1
            else:
                estado = 0
                

        elif estado == 4 and pos == 1: # levantarse a la izquierda
            if u < 14:
                akiha = pygame.image.load(Akihar_02[u]).convert_alpha()
                screen.blit(fondo,(0,0))
                screen.blit(akiha, (x, y))
                pygame.display.flip()
                pygame.time.wait(time_3)
                u += 1
            else:
                estado = 0

        elif estado == 5 and pos == 0: # arriba a la derecha
            while u < 27:
                if u <= 4:
                    akiha = pygame.image.load(Akiha_03[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
                    
                else:
                    if u <= 11:
                        akiha = pygame.image.load(Akiha_03[u]).convert_alpha()
                        screen.blit(fondo,(0,0))
                        screen.blit(akiha, (x, y))
                        pygame.display.flip()
                        pygame.time.wait(time_3)
                        u += 1
                        y -= 15
                    else:
                        if u <= 18:
                            akiha = pygame.image.load(Akiha_03[u]).convert_alpha()
                            screen.blit(fondo,(0,0))
                            screen.blit(akiha, (x, y))
                            pygame.display.flip()
                            pygame.time.wait(time_3)
                            u += 1
                            y += 15
                        else:
                            if u <27:
                                akiha = pygame.image.load(Akiha_03[u]).convert_alpha()
                                screen.blit(fondo,(0,0))
                                screen.blit(akiha, (x, y))
                                pygame.display.flip()
                                pygame.time.wait(time_3)
                                u += 1
                                
                            
            else:
                estado = 0

        elif estado == 5 and pos == 1: # arriba a la izquierda
            while u < 27:
                if u <= 4:
                    akiha = pygame.image.load(Akihar_03[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
                    
                else:
                    if u <= 11:
                        akiha = pygame.image.load(Akihar_03[u]).convert_alpha()
                        screen.blit(fondo,(0,0))
                        screen.blit(akiha, (x, y))
                        pygame.display.flip()
                        pygame.time.wait(time_3)
                        u += 1
                        y -= 15
                    else:
                        if u <= 18:
                            akiha = pygame.image.load(Akihar_03[u]).convert_alpha()
                            screen.blit(fondo,(0,0))
                            screen.blit(akiha, (x, y))
                            pygame.display.flip()
                            pygame.time.wait(time_3)
                            u += 1
                            y += 15
                        else:
                            if u <27:
                                akiha = pygame.image.load(Akihar_03[u]).convert_alpha()
                                screen.blit(fondo,(0,0))
                                screen.blit(akiha, (x, y))
                                pygame.display.flip()
                                pygame.time.wait(time_3)
                                u += 1
            else:
                estado = 0
                
        elif estado == 6 and pos == 0: # light punch derecha                   
            while u < 5:
                if u < 5:
                    akiha = pygame.image.load(Akiha_04[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
            else:
                estado = 0

        elif estado == 6 and pos == 1: # light punch izquierda                  
            while u < 5:
                if u < 5:
                    akiha = pygame.image.load(Akihar_04[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
            else:
                estado = 0
        elif estado == 7 and pos == 0: # media punch derecha                   
            while u < 5:
                if u < 5:
                    akiha = pygame.image.load(Akiha_05[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
            else:
                estado = 0

        elif estado == 7 and pos == 1: # media punch izquierda                  
            while u < 5:
                if u < 5:
                    akiha = pygame.image.load(Akihar_05[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
            else:
                estado = 0


        elif estado == 8 and pos == 0: # high kick derecha                   
            while u < 10:
                if u < 10:
                    akiha = pygame.image.load(Akiha_06[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
            else:
                estado = 0

        elif estado == 8 and pos == 1: # high kick izquierda                   
            while u < 10:
                if u < 10:
                    akiha = pygame.image.load(Akihar_06[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
            else:
                estado = 0

        elif estado == 9 and pos == 0: # salto hacia la derecha                  
            while u < 23:
                if u < 3:
                    akiha = pygame.image.load(Akiha_07[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
                else:
                    if u < 7:
                        akiha = pygame.image.load(Akiha_07[u]).convert_alpha()
                        screen.blit(fondo,(0,0))
                        screen.blit(akiha, (x, y))
                        pygame.display.flip()
                        pygame.time.wait(time_3)
                        u += 1
                        x += 15
                        y -= 20
                    else:
                        if u < 13:
                            akiha = pygame.image.load(Akiha_07[u]).convert_alpha()
                            screen.blit(fondo,(0,0))
                            screen.blit(akiha, (x, y))
                            pygame.display.flip()
                            pygame.time.wait(time_3)
                            u += 1
                            x += 25
                        else:
                            if u < 17:
                                akiha = pygame.image.load(Akiha_07[u]).convert_alpha()
                                screen.blit(fondo,(0,0))
                                screen.blit(akiha, (x, y))
                                pygame.display.flip()
                                pygame.time.wait(time_3)
                                u += 1
                                x += 15
                                y += 20
                            else:
                                if u < 23:
                                    akiha = pygame.image.load(Akiha_07[u]).convert_alpha()
                                    screen.blit(fondo,(0,0))
                                    screen.blit(akiha, (x, y))
                                    pygame.display.flip()
                                    pygame.time.wait(time_3)
                                    u += 1
                
            else:
                estado = 0          


        elif estado == 9 and pos == 1: # salto hacia la izquierda                 
            while u < 23:
                if u < 3:
                    akiha = pygame.image.load(Akihar_07[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
                else:
                    if u < 7:
                        akiha = pygame.image.load(Akihar_07[u]).convert_alpha()
                        screen.blit(fondo,(0,0))
                        screen.blit(akiha, (x, y))
                        pygame.display.flip()
                        pygame.time.wait(time_3)
                        u += 1
                        x -= 15
                        y -= 20
                    else:
                        if u < 13:
                            akiha = pygame.image.load(Akihar_07[u]).convert_alpha()
                            screen.blit(fondo,(0,0))
                            screen.blit(akiha, (x, y))
                            pygame.display.flip()
                            pygame.time.wait(time_3)
                            u += 1
                            x -= 25
                        else:
                            if u < 17:
                                akiha = pygame.image.load(Akihar_07[u]).convert_alpha()
                                screen.blit(fondo,(0,0))
                                screen.blit(akiha, (x, y))
                                pygame.display.flip()
                                pygame.time.wait(time_3)
                                u += 1
                                x -= 15
                                y += 20
                            else:
                                if u < 23:
                                    akiha = pygame.image.load(Akihar_07[u]).convert_alpha()
                                    screen.blit(fondo,(0,0))
                                    screen.blit(akiha, (x, y))
                                    pygame.display.flip()
                                    pygame.time.wait(time_3)
                                    u += 1
                
            else:
                estado = 0
                
        elif estado == 10 and pos == 0: # Burla                   
            while u < 13:
                if u < 13:
                    akiha = pygame.image.load(Akiha_08[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
            else:
                pygame.time.wait(250)
                estado = 0

        elif estado == 10 and pos == 1: # Burla                   
            while u < 13:
                if u < 13:
                    akiha = pygame.image.load(Akihar_08[u]).convert_alpha()
                    screen.blit(fondo,(0,0))
                    screen.blit(akiha, (x, y))
                    pygame.display.flip()
                    pygame.time.wait(time_3)
                    u += 1
            else:
                pygame.time.wait(250)
                estado = 0

                
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
                    
if __name__== "__main__":
    main()
                        
                        
