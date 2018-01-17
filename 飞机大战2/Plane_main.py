import pygame
from Plane_sprites import * 

list0 = [] 
class PlaneGame(object):

	def __init__(self):
		print('游戏初始化')
		self.init = pygame.init()
		#创建游戏窗口
		#.size取宽高  .x .y
		self.screen = pygame.display.set_mode((SCREEN_RECT.size))
		#创建游戏时钟
		self.clock = pygame.time.Clock()
		#调用私有方法，创建精灵和精灵组
		
		self.enemy_group = pygame.sprite.Group()
		self.enemy = Enemy()
		self.enemy_group.add(self.enemy)
		self.__create_sprites()
		self.enemy.kill()
		
		#设置定时器事件
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		#0.5打豆豆
		#pygame.time.set_timer(HERO_FIRE_EVENT,500)
		#self.enemy = None
		#self.enemy.speed = 0
	def start_game(self):
		print('开始游戏')

		while True:
			#1、设置频率
			self.clock.tick(60)
			#2、事件监听
			self.__event_handler()
			#3、碰撞检测
			self.__check_collide()
			#4、更新精灵组
			self.__update_sprites()
			#5、更新屏幕显示
			pygame.display.update()
			

	def __create_sprites(self):
		#创建精灵和精灵组
		#1、背景精灵组
		bg1 = Backgroup('/home/zhangjiayi/桌面/飞机大战/image/666/images/background.png')
		bg2 = Backgroup('/home/zhangjiayi/桌面/飞机大战/image/666/images/background.png')
		bg2.rect.y = -bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1,bg2)
		#2、敌人精灵组
		
		self.enemy_group = pygame.sprite.Group()
		#3、英雄精灵组
		self.hero = Hero()
		self.hero2 = Hero2()
		self.hero_group = pygame.sprite.Group()

		#print(self.enemy.speed)
		if self.enemy.speed == 2 :
			self.enemy.fire()
			#print('hahahahaha')
	def __event_handler(self):
		#事件监听
		
		key_pressed = pygame.key.get_pressed()
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT or key_pressed[113]:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				#print('敌机出场')
				self.enemy = Enemy()
				self.enemy_group.add(self.enemy)
			#elif event.type == HERO_FIRE_EVENT:
				#self.hero.fire()

				if self.enemy.speed == 2 :
					self.enemy.fire()
					#print('hahahahaha')

			if key_pressed[13]:
				#self.hero = Hero()
				#self.hero2 = Hero2()
				self.hero_group = pygame.sprite.Group(self.hero,self.hero2)
			#print(key_pressed)
			if key_pressed[106]:
				self.hero2.fire2()
			elif key_pressed[257]:
				self.hero.fire()

			elif key_pressed[275]:
				#print('向右移动')
				self.hero.speed = 2
			elif key_pressed[276]:
				#print('向左移动')
				self.hero.speed = -2

			elif key_pressed[100]:
				#print('向右移动')
				self.hero2.speed = 2
			elif key_pressed[97]:
				#print('向左移动')
				self.hero2.speed = -2

			else:
				self.hero.speed = 0
				self.hero2.speed = 0
		#if self.enemy.bullet3 != [] : 
			#print(self.enemy.ebullet.rect)
	def __check_collide(self):
		
		#子弹摧毁飞机
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True) 
		pygame.sprite.groupcollide(self.hero2.bullets2,self.enemy_group,True,True)
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy.bullets3,True,True) 
		pygame.sprite.groupcollide(self.hero2.bullets2,self.enemy.bullets3,True,True) 

		#飞机摧毁英雄
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		enemies2 = pygame.sprite.spritecollide(self.hero2,self.enemy_group,True)
		enemies3 = pygame.sprite.spritecollide(self.hero,self.enemy.bullets3,True)
		enemies4 = pygame.sprite.spritecollide(self.hero2,self.enemy.bullets3,True)
		#if enemies != None :
			#list0.append(enemies[-1])
		#if enemies != {}:
			#print(enemies)
		#if enemies != []:
			#list0.extend[enemies]
		#if enemies2 != [] :
			#list0.extend[enemies2]
			

		#判断列表是否有内容
		if len(enemies) > 0 :
			self.hero.kill()
			#enemies = []

			PlaneGame.__game_over()
		if len(enemies2) > 0 :
			self.hero2.kill()
			PlaneGame.__game_over()
		if len(enemies3) > 0 :
			self.hero.kill()
			PlaneGame.__game_over()
		if len(enemies4) > 0 :
			self.hero2.kill()
			PlaneGame.__game_over()
		#if len(enemies)>0 and len(enemies2) > 0 :
			#PlaneGame.__game_over()
		#if len(list0) == 2 :
			#PlsneGame.__game_over()

	def __update_sprites(self):
		#更新精灵组
		for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets,self.hero2.bullets2,self.enemy.bullets3]:
			#更新位置
			group.update()
			#绘制到屏幕上
			group.draw(self.screen)
		

	@staticmethod
	def __game_over():
		#游戏结束
		print('游戏结束')
		pygame.quit()
		exit()
		
#测试代码
if __name__ == '__main__':
	#创建游戏对象
	game = PlaneGame()
	#调用开始游戏的方法
	game.start_game()





