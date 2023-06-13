import pygame, math
from tkinter import simpledialog, messagebox


#Configurações iniciais
pygame.init()
tamanho = (883,600) 
branco = (255,255,255)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
running = True
icone = pygame.image.load("icon.bmp")
pygame.display.set_icon( icone )
fundo  = pygame.image.load("BG.bmp")
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
primeiraMensagem = False



while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            if bool(estrelas):
                resposta = messagebox.askyesno("Space Marker", "Deseja salvar os pontos antes de sair?")
                if resposta:
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
                #Marcação de distancias entre os pontos
                x,y = pos
                x_anterior, y_anterior = posicaoAnterior
                distancia = math.sqrt((x_anterior - x) ** 2 + (y_anterior - y) ** 2)
                distancia_texto = f'Distância: {distancia:.2f}'
                fonte = pygame.font.Font(None, 20)
                texto = fonte.render(distancia_texto, True, (255, 255, 255))
                posicao_texto = ((x + x_anterior) // 2, (y + y_anterior) // 2)
                tela.blit(texto, posicao_texto)
                

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
            else:
                messagebox.showinfo("Space Marker", "Não existem dados na tela para salvamento")
        

        #Carregamento
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            try:
                arquivo = open("RegistroDeEstrelas.txt","r")
                registro = arquivo.read()
                dicionario = eval(registro)
                estrelas = eval(registro)

                nomeAnterior = None

                for key,value in dicionario.items():      
                    pygame.draw.circle(tela, branco,(value), 5)
                    dicionario_chave = font.render(key, True, branco)
                    tela.blit(dicionario_chave, (value))
                    if nomeAnterior is not None:
                        pygame.draw.line(tela,branco,(value),(nomeAnterior),1)

                        #Marcação de distancias entre os pontos
                        x,y = value
                        x_anterior, y_anterior = nomeAnterior
                        distancia = math.sqrt((x_anterior - x) ** 2 + (y_anterior - y) ** 2)
                        distancia_texto = f'Distância: {distancia:.2f}'
                        fonte = pygame.font.Font(None, 20)
                        texto = fonte.render(distancia_texto, True, (255, 255, 255))
                        posicao_texto = ((x + x_anterior) // 2, (y + y_anterior) // 2)
                        tela.blit(texto, posicao_texto)

                    
                    nomeAnterior = value
            except:
               messagebox.showinfo("Space Marker", "Não existem dados salvos para carregamento")

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
    if primeiraMensagem == False:
        messagebox.showinfo("Space Marker", "Verifique se há dados salvos antes de realizar novas marcações")
        primeiraMensagem = True
pygame.quit()