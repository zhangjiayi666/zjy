import random
import pygame
from Plane_main import *

pygame.mixer.init()
pygame.mixer.music.load('/home/zhangjiayi/音乐/CloudMusic/666.mp3')
pygame.mixer.music.play(1)




#游戏屏幕的大小
SCREEN_RECT = pygame.Rect(0,0,480,700)
#敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#定义子弹的常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1) :
		#调用父类的方法
		super().__init__()

		#加载图像
		self.image = pygame.image.load(image_name)

		#设置尺寸
		self.rect = self.image.get_rect()

		#记录速度
		self.speed = speed

	def update(self):
		
		#默认在垂直方向移动
		self.rect.y += self.speed

class Backgroup(GameSprite):
	
	def update(self):
		super().update()
		
		#判断是否移出屏幕
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):
	def __init__(self):
		#1、调用父类方法，创建敌机精灵，指定图像
		super().__init__('/home/zhangjiayi/桌面/飞机大战/image/666/images/enemy1.png')
		
		self.bullets3 = pygame.sprite.Group()
		#2、随机初始速度
		self.speed = random.randint(1,3)
		#3、随机初始位置:
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)

	def update(self):
		#1、调用父类方法，垂直移动
		super().update()

		#2、判断飞机是否飞出屏幕，是则删除
		if self.rect.y >= SCREEN_RECT.height:
			#print('飞机已经销毁')
			self.kill()
	def fire(self):
		#print('豆豆')
		#for i in (1,2,3):
		ebullet = Ebullet()
		ebullet.rect.bottom = self.rect.y + 20#*i
		ebullet.rect.centerx = self.rect.centerx
		self.bullets3.add(ebullet)

	def __del__(self):
		#print('敌机挂掉了%s'%self.rect)
		pass

class Hero(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/飞机大战/image/666/images/life.png',0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		
		self.bullets = pygame.sprite.Group()

	def update(self):
		self.rect.x += self.speed

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		#print('豆豆')
		#for i in (1,2,3):
		bullet = Bullet()
		bullet.rect.bottom = self.rect.y - 20#*i
		bullet.rect.centerx = self.rect.centerx
		self.bullets.add(bullet)

class Hero2(GameSprite):
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/飞机大战/image/666/images/life.png',0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		
		self.bullets2 = pygame.sprite.Group()

	def update(self):
		self.rect.x += self.speed

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire2(self):

		#print('66666666')
		bullet2 = Bullet2()
		bullet2.rect.bottom = self.rect.y - 20 
		bullet2.rect.centerx = self.rect.centerx
		self.bullets2.add(bullet2)

class Bullet(GameSprite):
	
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/飞机大战/image/666/images/bullet2.png',-3)
	def __del__(self):
			print('子弹删除')
			#pass
	def update(self):
		self.rect.y += self.speed
		if self.rect.bottom < 0 :
			self.kill()
class Bullet2(GameSprite):
	
	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/飞机大战/image/666/images/bullet1.png',-3)
	def __del__(self):
			#print('子弹删除')
			pass
	def update(self):
		self.rect.y += self.speed
		if self.rect.bottom < 0 :
			self.kill()
class Ebullet(GameSprite):

	def __init__(self):
		super().__init__('/home/zhangjiayi/桌面/飞机大战/image/666/images/bomb_supply.png',15)
	def __del__(self):
		#print('子弹没了')
		pass
	def update(self):
		super().update()
		#self.rect.y += self.speed
		if self.rect.y > 700:
			self.kill()
