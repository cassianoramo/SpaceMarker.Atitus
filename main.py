import pygame
from tkinter import simpledialog, messagebox


#Configurações iniciais
pygame.init()
tamanho = (883,600)
branco = (255,255,255)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
running = True
icone = pygame.image.load("icon.png")
pygame.display.set_icon( icone )
fundo  = pygame.image.load("BG.jpeg")
pygame.mixer.music.load("Interstellar.mp3")
pygame.mixer.music.play(-1)

#Variaveis de renderização
font = pygame.font.Font(None, 20)
tela.blit( fundo, (0,0) )
salvar = font.render("Pressione F10 para Salvar os pontos", True, branco)
carregar = font.render("Pressione F11 para Carregar os pontos", True, branco)
deletar = font.render("Pressione F12 para Deletar os pontos", True, branco)
tela.blit( salvar, (10, 10) )
tela.blit( carregar, (10, 22) )
tela.blit( deletar, (10, 32) )
#Variaveis dos pontos
estrelas = {}
dicionario = {}
posicaoAnterior = (0,0)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            if bool(estrelas):
                estrelas.update(dicionario)
                arquivo = open("RegistroDeEstrelas.txt","w")
                arquivo.write(str(estrelas))
                arquivo.close()
            running = False
        #Caixa de Diálogo
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space","Nome da Estrela: ")
            print(item)
            if item == "":
                item = "desconhecido"+str(pos)
            if item == None:
                break
            estrelas[item] = pos
            pygame.draw.circle(tela, branco,(pos),5)
            if posicaoAnterior != (0,0):
                pygame.draw.line(tela,branco,(pos),(posicaoAnterior),1)
            estrelaNome = font.render(item, True, branco)
            tela.blit(estrelaNome, (pos) )
            posicaoAnterior = pos

        #Salvamento
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10: 
            if bool(estrelas):
                estrelas.update(dicionario)
                arquivo = open("RegistroDeEstrelas.txt","w")
                arquivo.write(str(estrelas))
                arquivo.close()
        

        #Carregamento
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            try:
                arquivo = open("RegistroDeEstrelas.txt","r")
                registro = arquivo.read()
                dicionario = eval(registro)

                nomeAnterior = None

                for key,value in dicionario.items():      
                    pygame.draw.circle(tela, branco,(value), 5)
                    dicionario_chave = font.render(key, True, branco)
                    tela.blit(dicionario_chave, (value))
                    if nomeAnterior is not None:
                        pygame.draw.line(tela,branco,(value),(nomeAnterior),1)
                    nomeAnterior = value
            except:
               messagebox.showinfo("Space Marker", "Não existem dados salvos")

        #Delete
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            arquivo = open("RegistroDeEstrelas.txt", "w")  
            arquivo.truncate()  
            arquivo.close()  
            estrelas = {}
            dicionario = {}
            posicaoAnterior = (0,0)
            tela.blit( fundo, (0,0) )
            tela.blit( salvar, (10, 10) )
            tela.blit( carregar, (10, 22) )
            tela.blit( deletar, (10, 32) )



    pygame.display.update()
pygame.quit()