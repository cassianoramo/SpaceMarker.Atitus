import pygame

#Configurações iniciais
pygame.init()
tamanho = (883,600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
running = True
icone = pygame.image.load("icon.png")
pygame.display.set_icon( icone )
fundo  = pygame.image.load("BG.jpeg")
pygame.mixer.music.load("Interstellar.mp3")
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    tela.blit( fundo, (0,0) )
    pygame.display.update()
pygame.quit()