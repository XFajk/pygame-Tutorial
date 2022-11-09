import pygame 

pygame.init()

window = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

# variables
x = 100
obdlznik = pygame.Rect(x,200,100,50)

running = True
while running:

	obdlznik = pygame.Rect(x,200,100,50)

	window.fill((255,255,255))

	pygame.draw.rect(window,(255,0,0),obdlznik)
	x += 1

	pygame.display.update()

	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			running = False	

	clock.tick(60)
	pygame.display.set_caption(f"game window FPS: {int(clock.get_fps())}")



pygame.quit()