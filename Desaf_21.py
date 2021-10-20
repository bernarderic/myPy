#faça um programa que abra e reproduza um arquivo mp3
############################################################
import pygame
#import os
pygame.init()
pygame.mixer.music.load('CLE.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)
clock = pygame.time.Clock()
clock.tick(10)

while pygame.mixer.music.get_busy():
     pygame.event.poll()
     clock.tick(10)
else:
  print('O arquivo musica.mp3 não está no diretório do script Python')