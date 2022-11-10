import pygame 

pygame.init()

ZOOM = 1
WS = (800,600)
DS = (WS[0]/ZOOM,WS[1]/ZOOM)

window = pygame.display.set_mode(WS)
display = pygame.Surface(DS)

clock = pygame.time.Clock()

# variables
x = 100
obdlznik = pygame.Rect(x,200,100,50)

running = True
while running:

	obdlznik = pygame.Rect(x,200,100,50)

	display.fill((255,255,255))

	pygame.draw.rect(display,(255,0,0),obdlznik)
	x += 1

	pygame.display.update()

	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			running = False	

	surf = pygame.transform.scale(display,WS)
	window.blit(surf, (0,0))
	clock.tick(60)
	pygame.display.set_caption(f"game window FPS: {int(clock.get_fps())}")



pygame.quit()