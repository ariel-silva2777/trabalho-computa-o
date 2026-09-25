import pygame
import os
import random
pygame.init()
#variaveis globais
tela_Altura = 600
tela_Largura = 1100
tela = pygame.display.set_mode((tela_Largura,tela_Altura))

branco = pygame.Color(255,255,255)
vermelho = pygame.Color(255,0,0)
azul = pygame.Color(0,0,255)
verde = pygame.Color(0,255,0)
corredorr = [pygame.image.load("pixil-frame-0.png"),
pygame.image.load("pixil-frame-1.png"),
pygame.image.load("pixil-frame-2.png"),
pygame.image.load("pixil-frame-3.png"),
pygame.image.load("pixil-frame-4.png"),
pygame.image.load("pixil-frame-5.png"),
pygame.image.load("pixil-frame-6.png"),
pygame.image.load("pixil-frame-7.png"),
pygame.image.load("pixil-frame-8.png"),
pygame.image.load("pixil-frame-9.png"),
pygame.image.load("pixil-frame-10.png"),
pygame.image.load("pixil-frame-11.png"),]
chao = pygame.image.load("grama123-atualizada-pixilart.png")
carro = pygame.transform.scale((pygame.image.load("image-removebg-preview.png")),(100,100))
#animações

#base = [  pygame.image.load(os.path.join())  ]

class runner():
    pos_y = 400
    pos_x = 310
    pos_y_abaixado = pos_y + 10
    veloz_pulo = 8
    def __init__(self):
        #sprites
        #bases
        #self.NomeDaAnimacao = VariavelQueEstaOCaminhoDaImagem
        self.correrimg = corredorr
        self.pularimg = corredorr
        self.abaixarimg = corredorr
        
        #self.NomeDaAnimacao = True ou False para deixa ativa quando inicia o jogo
        self.correndo = True
        self.pulando =False
        self.abaixando = False
        
        
        self.step_index = 0
        self.velocidade_pulo = self.veloz_pulo
        self.img = self.correrimg[0]
        #self.runner_Colision = self.image.get_rect()
        self.runner_CordY = self.pos_y
        self.runner_CordX = self.pos_x
        
    def pular(self):
        self.img = self.pularimg[self.step_index]
        #self.runner_Colision = self.image.get_rect()
        if self.pulando:
            self.runner_CordY -= self.velocidade_pulo * 4
            self.velocidade_pulo -= 0.5
        if self.velocidade_pulo < -self.veloz_pulo:
            self.velocidade_pulo = self.veloz_pulo
            self.pulando = False
        
    def abaixar(self):
        self.img = self.abaixarimg[self.step_index]
        #self.runner_Colision = self.image.get_rect()
        self.runner_CordY = self.pos_y
        self.runner_CordX = self.pos_x
        self.step_index +=1
    def correr(self):
        self.img = self.correrimg[self.step_index]
        #self.runner_Colision = self.image.get_rect()
        self.runner_CordY = self.pos_y_abaixado
        self.runner_CordX = self.pos_x
        self.step_index +=1
        
        
    def update(self, input):
        
        if self.abaixando:
            self.abaixar()
            
        if self.pulando:
            self.pular()
            
        if self.correndo:
            self.correr()
            
            
            
            
        if self.step_index >= 11:
            self.step_index = 0
            
                   
        if input[pygame.K_UP] and not self.pulando:
            self.correndo = False
            
            self.pulando= True
            
            self.abaixando = False
        elif input[pygame.K_DOWN] and not self.abaixando:
            self.correndo = False
            
            self.pulando = False
            
            self.abaixando = True
        elif not (self.pulando or input[pygame.K_DOWN]):
            self.correndo = True
            
            self.pulando = False
            
            self.abaixando = False


    def draw(self,tela):
        tela.blit(self.img,(self.runner_CordX, self.runner_CordY))
    pass

class objetos_():
    def __init__(self):
        self.sprite = carro
        self.pos_x = tela_Largura + random.randint(800,1000)
        self.pos_y = 400
        #self.text = 
        self.width= 0
        
    def update(self):
        self.pos_x -= gamespeed
        if self.pos_x <self.width:
            self.pos_x = tela_Largura + random.randint(2500,3000)
            self.pos_y = 400
        
    def draw(self,tela):
        tela.blit(self.sprite,(self.pos_x,self.pos_y))

class obstaculos():
    def __init__(self,imagem,typo):
        self.textura = imagem
        self.type = typo
        self.rect = self.textura[self.type].get_rect()
        self.rect.x = tela_Largura
    def update(self):
        self.pos_x -= gamespeed
        if self.pos_x <self.width:
            obstaculos.pop()
            
    def draw(self,tela):
        tela.blit(self.textura,(self.pos_x,self.pos_y))

class obstaculo_curto(obstaculos):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.pos_obst_y = 360
        self.pos_obst_x = tela_Largura
class obstaculo_longo(obstaculos):
    def __init__(self,image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type)
        self.pos_obst_y = 360
        self.pos_obst_x = tela_Largura
def main ():
    global gamespeed , pos_x_bg , pos_y_bg, pontos
    run = True
    clock = pygame.time.Clock()
    player = runner()
    objs = objetos_()
    #obstaculo = obstaculos(carro,0)
    gamespeed = 14
    pos_x_bg = 0
    pos_y_bg = 500
    pontos = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    def placar():
        global pontos, gamespeed
        pontos += 1
        if pontos % 100 == 0:
            gamespeed +=0.1
        text = font.render("pontuação: "+str(pontos), True,(0,0,0))
        textRect = text.get_rect()
        textRect.center = (1000,40)
        tela.blit(text,textRect)
    def background():
        global pos_x_bg, pos_y_bg
        bg_width = chao.get_width() #usar o metodo get_width para definir isso
        tela.blit(chao,(pos_x_bg,pos_y_bg))
        tela.blit(chao,(pos_x_bg + bg_width ,pos_y_bg))
        if pos_x_bg <= -bg_width:
            tela.blit(chao,(pos_x_bg + bg_width ,pos_y_bg),)
            pos_x_bg  = 0
        pos_x_bg -= gamespeed
        
        
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #steps // coisas que acontecem a acada loop do jogo
        tela.fill(branco)
        tecla = pygame.key.get_pressed()
            
        player.draw(tela)
        player.update(tecla)
        objs.draw(tela)
        objs.update()
        #obstaculo.draw(tela)
        #obstaculo.update()
        placar()
        background()
        pygame.display.update()
            
        clock.tick(60)
    pygame.quit()
main()
            
            
            
