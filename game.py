import pygame
import time
from random import randint

Q = []

entities = ["Scientist", "Girl", "Boy", "Lion", "Cow", "Bag"]
prohibited = [(1,3),(2,3),(1,4),(2,4),(3,4),(4,5)]
error_dict = {}

def permute(s,n):
    seq = range(s)
    permutations = []
    nodes = list(seq)
    while len(permutations) < s**n:
        node = nodes.pop(0)
        children = list(seq)
        permutation = permutations.pop(0) if len(permutations)>1 else []
        for i in range(len(children)):
            perm = list(permutation)
            perm.append(children[i])
            permutations.append(perm)
            nodes.append(children[i])
    return permutations

Qx = lambda q: Q.index(q)
E = [ (i, 0, j, k) for i in [1,0] for j in range(6) for k in range(6) ]
T = lambda q, i: [ i[0] if i[1] == j or i[2] == j or i[3] == j else q[j] for j in range(len(q))]
valid = lambda q: not (sum([q[p[0]]==q[p[1]] and q[0]!=q[p[0]] for p in prohibited]) > 0)
transition = lambda q: [ (e, Qx( T(q,e) )) for e in E if e[0]!=q[0] and e[0]!=q[e[2]] and e[0]!=q[e[3]]]
valid_transitions = lambda q: [ n for n in transition(q) if valid(Q[n[1]]) ]

Q = permute(2,6)
F = Q[-1]

curr_state = Q[0]
curr_planet = 0

pygame.init()

# Global Variables
width = 1920
height = 900


# Colors
black = (0,0,0)
white = (255, 255, 255)
red = (180, 0, 0)
green = (0, 200, 0)
light_red = (255, 0, 0)
light_green = (0, 255, 0)
aqua = (0, 255, 255)

# Initialization
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Crossing Planets')
clock = pygame.time.Clock()

# Sprites
bg = pygame.image.load('res/bg1.png')
graph = pygame.transform.scale(pygame.image.load('Figure_1.png'), (1045, 900))

class Object:

	def __init__(self,  img, x, y, w, h):
		self.img, self.x, self.y, self.w,self.h  = img, x, y, w, h
		
	def render(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		if (self.x + self.w) > mouse[0] > self.x and (self.y + self.h) > mouse[1] > self.y:
			
			if click[0] == 1:
				#print(len(sr.get_passenger_list()) )
				if len(sr.get_passenger_list()) < 3:
					if isinstance(self, Scientist):
						sr.add_passenger(self)
						print(sr.passenger_list)
						self.y = 2000
					elif isinstance(self, Girl):
						sr.add_passenger(self)
						self.y = 2000
					elif isinstance(self, Boy):
						sr.add_passenger(self)
						self.y = 2000
					elif isinstance(self, Lion):
						sr.add_passenger(self)
						self.y = 2000
					elif isinstance(self, Cow):
						sr.add_passenger(self)
						self.y = 2000
					elif isinstance(self, Bag):
						sr.add_passenger(self)
						self.y = 2000
				else:
					print("Rocket Full!")
					
		gameDisplay.blit(self.get_img(),(self.get_x(), self.get_y()))
		
	def set_img(self, img):
		self.img = img
	
	def get_img(self):
		return self.img

	def set_x(self, x):
		self.x = x
	
	def get_x(self):
		return self.x
		
	def set_y(self, y):
		self.y = y
	
	def get_y(self):
		return self.y
		
	def set_w(self, w):
		self.w = w
	
	def get_w(self):
		return self.w
		
	def set_h(self, h):
		self.h = h
	
	def get_h(self):
		return self.h

class Rocket(Object):

	def __init__(self):
		super().__init__(pygame.image.load('res/rocket3.png'), 700, 0, -1 , -1)
		self.passenger_list = []
		self.move = False

	def update(self):
		global curr_planet 
		global curr_state
		global gege
		if self.can_move():
			if curr_planet == 0:
				self.set_y(self.get_y() - 10)
				
				if self.y == -240:
					self.y = 1140
			elif curr_planet == 1:
				self.set_y(self.get_y() - 10)
			
			if self.get_y() == 650:
				curr_planet = 1
				self.set_move(False)
				self.unload_passengers()
				if not valid(curr_state):
					gege = True
					gg()
			elif self.get_y() == 0:
				curr_planet = 0
				self.set_move(False)
				self.unload_passengers()
				if not valid(curr_state):
					gege = True
					gg()
				
	def add_passenger(self, p):
		self.passenger_list.append(p)

	def remove_passenger(self, p):
		self.passenger_list.remove(p)
	
	def unload_passengers(self):
		global curr_planet
		
		if curr_planet == 0:
			for p in self.passenger_list:
				if isinstance(p, Scientist):
					p.set_y(60)
				elif isinstance(p, Girl):
					p.set_y(110)
				elif isinstance(p, Boy):
					p.set_y(100)
				elif isinstance(p, Lion):
					p.set_y(160)
				elif isinstance(p, Cow):
					p.set_y(140)
				elif isinstance(p, Bag):
					p.set_y(130)
					
			self.passenger_list.clear()
		elif curr_planet == 1:
			print(len(self.passenger_list))
			for p in self.passenger_list:
				print(self.passenger_list)
				if isinstance(p, Scientist):
					p.set_y(710)
				elif isinstance(p, Girl):
					p.set_y(750)
				elif isinstance(p, Boy):
					p.set_y(740)
				elif isinstance(p, Lion):
					p.set_y(790)
				elif isinstance(p, Cow):
					p.set_y(780)
				elif isinstance(p, Bag):
					p.set_y(770)

			self.passenger_list.clear()

	def get_passenger_list(self):
		return self.passenger_list

	def set_move(self, b):
		self.move = b
	
	def can_move(self):
		return self.move
		
class Scientist(Object):
	def __init__(self):
		super().__init__(pygame.image.load('res/scientist1.png'), 580, 60, 107, 180)
		
	def update(self, y):
		self.set_y(y)

class Boy(Object):
	def __init__(self):
		super().__init__(pygame.image.load('res/boy1.png'), 420, 100, 73, 151)
		
	def update(self, y):
		self.set_y(y)
		
class Girl(Object):
	def __init__(self):
		super().__init__(pygame.image.load('res/girl1.png'), 500, 110, 80, 139)
		
	def update(self, y):
		self.set_y(y)
		
class Lion(Object):
	def __init__(self):
		super().__init__(pygame.image.load('res/lion1.png'), 300, 160, 138, 97)
		
	def update(self, y):
		self.set_y(y)
		
class Cow(Object):
	def __init__(self):
		super().__init__(pygame.image.load('res/cow1.png'), 125, 140, 182, 123)
		
	def update(self, y):
		self.set_y(y)
		
class Bag(Object):
	def __init__(self):
		super().__init__(pygame.image.load('res/bag1.png'), 0, 130, 136, 129)
		
	def update(self, y):
		self.set_y(y)

sr = Rocket()		
s = Scientist()
g = Girl()
b = Boy()
l = Lion()
c = Cow()
bag = Bag()
game_over = False
gege = False

def render_figure():
	try:
		gameDisplay.blit(pygame.transform.scale(pygame.image.load('fig/{0}.png'.format(Qx(curr_state))), (1045, 900)),(875, 0))
	except:
		print("Figure not found!")
	
def render_bg():
	gameDisplay.blit(bg,(0, 0))
	
def launch_rocket():
	global curr_state
	global curr_planet
	input = ()
	
	if curr_planet == 0:
		input += (1,)
	else:
		input += (0,)
		
	# Update back end current state.	
	if s not in sr.get_passenger_list():
		print("Error scientist not in rocket")
	else:
		for p in sr.get_passenger_list():
			if isinstance(p, Scientist):
				input += (0,)
			elif isinstance(p, Girl):
				input += (1,)
			elif isinstance(p, Boy):
				input += (2,)
			elif isinstance(p, Lion):
				input += (3,)
			elif isinstance(p, Cow):
				input += (4,)
			elif isinstance(p, Bag):
				input += (5,)
		
		while len(input) < 4:
			input +=(0,)
		
		print(input)
		
		curr_state = T(curr_state, input)
		
		print(curr_state)
		sr.set_move(True)
		
def clear_passengers():
	sr.unload_passengers()

def hint():
	global curr_state
	print(curr_state)
	temp = valid_transitions(curr_state)
	r = randint(0, len(temp) - 1)
	
	h = "Board the Scientist, the {0}, and the {1}".format(entities[temp[r][0][2]], entities[temp[r][0][3]])
	
	message_display(h, 400, 375, 35, aqua)
	time.sleep(2)	
	
def text_objects(text, font, color):
	text_surface = font.render(text, True, color)
	return text_surface, text_surface.get_rect()
	
def message_display(m, x, y, s, r):
	large_text = pygame.font.Font("freesansbold.ttf", s)
	TextSurface, TextRect = text_objects(m, large_text, r)
	TextRect.center = (x,y)
	gameDisplay.blit(TextSurface, TextRect)
	
	pygame.display.update()
	
	#time.sleep(2)

def gg():
	global gege
	
	while gege:
		message_display("Game Over!", 400, 375, 115, aqua)
		#print("err msg")
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		button("Play Again", 150, 750, 130, 50, green, light_green, game_loop)
		button("Quit", 550, 750, 130, 50, red, light_red, quit_game)
		
		pygame.display.update()
		clock.tick(60)
	
def button(msg, x, y, w, h, i, a, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	#print(click)
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, a, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
			#if action == "play":
				#game_loop()
	else:
		pygame.draw.rect(gameDisplay, i, (x, y, w, h))
	
	small_text = pygame.font.Font("freesansbold.ttf", 20)
	TextSurface, TextRect = text_objects(msg, small_text, white)
	TextRect.center = ((x+(w/2)),(y+(h/2)))
	gameDisplay.blit(TextSurface, TextRect)

def quit_game():
	global game_over
	global gege
	gege = False
	game_over = True
	
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
		TextSurface, TextRect = text_objects("Crossing Planets", large_text, white)
		TextRect.center = ((width/2),(250))
		gameDisplay.blit(TextSurface, TextRect)
		
		button("PLAY", (width/2), 700, 100, 50, green, light_green, game_loop)
		
		pygame.display.update()
		
		clock.tick(60)
		
def game_loop():
	global game_over
	global curr_state
	global curr_planet
	curr_state = Q[0]
	curr_planet = 0
	
	while not game_over:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				game_over = True
				
			#print(e)
		
		gameDisplay.fill(black)
		render_figure()
		render_bg()
		
		button("LAUNCH", 900, 750, 100, 50, red, light_red, launch_rocket)
		button("CLEAR", 900 , 820, 100, 50, red, light_red, clear_passengers)
		button("HINT", 1020, 750, 100, 50, red, light_red, hint)
		button("SOLUTIONS", 1140, 750, 140, 50, red, light_red)
		button("RESET", 1020, 820, 100, 50, red, light_red)
		button("QUIT", 1140, 820, 100, 50, red, light_red, quit_game)
		
		sr.render()
		s.render()
		g.render()
		b.render()
		l.render()
		c.render()
		bag.render()
		
		sr.update()
		
		# Refresh

		pygame.display.update()
		clock.tick(60)

def main():
	#game_intro()
	game_loop()
	pygame.quit()
	quit()
	
if __name__ == '__main__':
	main()	