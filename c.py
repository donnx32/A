import pygame

pygame.init()

# Global Variables
width = 1920
height = 900

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)

# initialization
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Crossing Planets')
clock = pygame.time.Clock()

# Images
bg = pygame.image.load('bg1.png')
graph = pygame.transform.scale(pygame.image.load('Figure_1.png'), (1045, 900))
rocket = pygame.image.load('res/rocket3.png')
scientist = pygame.transform.scale(pygame.image.load('res/scientist.png'), (122, 186))

def render_figure():
	gameDisplay.blit(graph,(875, 0))
	
def render_bg():
	gameDisplay.blit(bg,(0, 0))
	
def render_rocket():
	gameDisplay.blit(rocket,(0, 0))
	
def render_scientist():
	gameDisplay.blit(scientist,(420, 710))
	
def text_objects(text, font):
	text_surface = font.render(text, True, white)
	return text_surface, text_surface.get_rect()
	
def message_display(s):
	large_text = pygame.font.Font("freesansbold.ttf", 115)
	TextSurface, TextRect = text_objects(s, large_text)
	TextRect.center = ((width/2),(height/2))
	gameDisplay.blit(TextSurface, TextRect)
	
	pygame.display.update()
	
	#time.sleep(2)

def gg():
	message_display("Game Over!")
	
def game_intro():
	intro = True
	
	while intro:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				quit()
	
		gameDisplay.fill(black)
		gameDisplay.blit(pygame.transform.scale(pygame.image.load('res/space.jpg'), (1920, 900)),(0, 0))
		
		large_text = pygame.font.Font("freesansbold.ttf", 115)
		TextSurface, TextRect = text_objects("Crossing Planets", large_text)
		TextRect.center = ((width/2),(250))
		gameDisplay.blit(TextSurface, TextRect)
		
		pygame.display.update()
		clock.tick(15)
		
def game_loop():
	game_over = False
	while not game_over:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				game_over = True
				
			#print(e)
		
		gameDisplay.fill(black)
		render_figure()
		render_bg()
		render_rocket()
		render_scientist()
		
		gg()
		# Refresh
		pygame.display.update()
		clock.tick(60)

def main():
	game_intro()
	game_loop()
	pygame.quit()
	quit()
	
if __name__ == '__main__':
	main()	