# 小试牛刀文件
# 运行下列代码
import pygame,sys
from pygame.locals import *
import easygui
import os

pygame.init()
canvas = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("寻找宝藏")

bg=pygame.image.load("images/find-bg.png")
end=pygame.image.load("images/end.png")

canvas.blit(bg,(0,0))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			mouseX = pos[0]
			mouseY = pos[1]
			print(pos)
			if 430 < mouseX < 520 and 165 < mouseY < 255:
				canvas.blit(end,(0,0))
				pygame.display.update()
			else:
				os.system(r'python tools/box.py')

	pygame.display.update()