'''
import sys, pygame
pygame.init()

# Espaço pra Introduzir variaveis estaticas, dar loading...
size = width, height = 1280,720 #Tamanho da tela de 600x600px
screen = pygame.display.set_mode(size)

black = 0,0,0 #RED, GREEN, BLUE (cor)
white = 255,255,255 #(cor)
vermelho = 255,0,0 #(cor)
roxo = 255,0,255 #(cor)

ball = pygame.image.load("intro_ball.gif") #textura, mas falta a geometria(colision box)
ballrect = ball.get_rect() #representa o hitbox da ball 
ballrect.center = (400,200) #não aparecer na corrdenada 0,0(padrão) quando o jogo é iniciadop

background = pygame.image.load("grass.jpg") # a imagem tem q ta na mesma pasta

font = pygame.font.Font("freesansbold.ttf", 50) #(name, size)
text = font.render("Game OVER!!!", True, (255,255,0), (0,0,0)) #mensagem, n sei, escolhar a cor RGB do text, escolher a cor do backgroud do texto
textRect - text.get_rect(); #rentagulo variavel de texto
textRect,center = (600,600) #coloci o retangulo no meio da tela

clock = pygame.time.Clock()
myhp = 0

while True: #Criar um loop infinito
	for event in pygames.event.get():
		if event.type == pygame.QUIT: 
			sys.exit() #identação ta na mesma linha, pra fazer tu sair do jogo normal
		'''
		'''
		if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			ballrect = ballrect.move(20, 0) #mover a bolinha dentro das cordenadas q eu passar
		if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			ballrect = ballrect.move(-20, 0)
		if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			ballrect = ballrect.move(0,-20) #Negativo? pois é, na tela ela funciona como o plano carteisano, mas cresce indo de cima pra baixo e da esquerda pra direita
		if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			ballrect = ballrect.move(0,20)	
		#aperta uma vez, 1 movimento
		'''
		'''
    #enquanto eu presionar, ela se move(melhor):
	pressed = pygame.key.get_pressed() #o q ta sendo apertado
	if pressed[pygame.K_UP] and ballrect.top > 0:
		ballrect = ballrect.move(0,-20)
	if pressed[pygame.K_DOWN] and ballrect.bottom < height:
		ballrect = ballrect.move(0,20)
	if pressed[pygame.K_LEFT] and ballrect.left > 0:
		ballrect = ballrect.move(-20,0)
	if pressed[pygame.K_RIGHT] and ballrect.right < width:
		ballrect = ballrect.move(20,0)				
    #Vai sumir com a bola pq n definimos o frmaes per second, vamos usar o clock p corrigir isso
    #A bola ainda some, so que ao nosso controle, vamos adicionar "colisão";

#    my_hp_text = font.render("Segundos:{0}".format(myhp), True, (255,255,0), (0,0,0))
#    my_hp_text_rect = my_hp_text.get_rect()
#    my_hp_text_rect.center = (200,50)	

    #myhp = myhp + 1

    clock.tick(60) #60fps
    screen.fill(white) #sem isso se a bola sair do background, ela vai ficar meio que se reptindo
    screen.blit(background,(0,0)) #tenha em mente a resolução da imagem q tu pega
	#screen.fill(vermelho) #vai cobrir toda a tela de vermelho
	screen.blit(ball, ballrect) #atualizar a textura pro local q o hotbxo tiver		
	screen.blit(text, textRect)
#	screen.blit(my_hp_text, my_hp_text_rect)
	pygame.display.flip() #No final do laço, ele vai atualizar a tela; 
'''



















import sys, pygame
pygame.init()

size = width, height = 1280,720
screen = pygame.display.set_mode(size)
white = 255,255,255 #RED, GREEN, BLUE 

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
ballrect.center = (400,200) 

background = pygame.image.load("grass.jpg")

font = pygame.font.Font("freesansbold.ttf", 50)
text = font.render("Game OVER!!!", True, (255,255,0), (0,0,0))
textRect = text.get_rect();
textRect.center = (600,600)


clock = pygame.time.Clock()
myhp=0

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()
       if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
           ballrect = ballrect.move(20,0)
       if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
           ballrect = ballrect.move(-20,0)
       if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
           ballrect = ballrect.move(0,-20)    
       if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
           ballrect = ballrect.move(0,20)
           
     
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and ballrect.top > 0:
        ballrect = ballrect.move(0,-20)
    if pressed[pygame.K_DOWN] and ballrect.bottom < height :
        ballrect = ballrect.move(0,20)
    if pressed[pygame.K_LEFT] and ballrect.left > 0:
        ballrect = ballrect.move(-20,0)
    if pressed[pygame.K_RIGHT] and ballrect.right < width:
        ballrect = ballrect.move(20,0)
        
        
    my_hp_text = font.render("Segundos:{0}".format(myhp), True, (255,255,0), (0,0,0))
    my_hp_text_rect = my_hp_text.get_rect()
    my_hp_text_rect.center = (200,50)
    
    myhp = myhp+1
    
    clock.tick(360)
    screen.fill(white)
    screen.blit(background,(0,0))
    screen.blit(ball,ballrect)
    screen.blit(text,textRect)
    screen.blit(my_hp_text,my_hp_text_rect)
    pygame.display.flip()




