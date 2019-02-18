import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CRESTR_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    '''飞机大战游戏精灵'''

    def __init__(self,imge_name,speed = 3):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(imge_name)
        self.rect = self.image.get_rect()
        self.speed = speed


    def update(self):

        #在屏幕上垂直方向移动
        self.rect.y += self.speed



class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self,flag = False):
        """

        :param flag: 标记滚动图片
        """
        super().__init__("./images/background.png")
        if flag:
            self.rect.y = -self.rect.height



    def update(self):
        # 1 调用父类方法移动背景
        super().update()
        # 2 判断是否移除屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):

    def __init__(self):
        # 调用父类创建敌机，指定图片
        super().__init__("./images/enemy1.png")
        # 设置随机速度
        self.speed = random.randint(1,3)
        # 设置随机位置
        enemy_max_x = SCREEN_RECT.width - self.rect.width
        self.rect.bottom = 0
        self.rect.x = random.randint(1,enemy_max_x)
        # 死亡图片列表
        self.diels = [("images/enemy1_down"+str(i)+".png") for i in range(1,5)]


    def update(self):

        # 调用父类方法
        super().update()
        # 飞出，删除
        if self.rect.y >=SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        pass

class Hero(GameSprite):
    '''英雄精灵'''

    def __init__(self):
        super().__init__("./images/me1.png")
        self.speed = 0
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

        # 死亡图片列表
        self.diels = [("images/me_destroy_" + str(i) + ".png") for i in range(1, 5)  ]
        

    def update(self):

        if (self.rect.x+self.speed >=0 and self.rect.x+self.speed <= SCREEN_RECT.width - self.rect.width):
            self.rect.x += self.speed

    def fire(self):
        # 创建子弹精灵
        for i in (0,1,2):
            bullet = Bullet()
            # 设置子弹位置
            bullet.rect.bottom = self.rect.y - 15*i
            bullet.rect.centerx = self.rect.centerx
            # 添加达到精灵组
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹"""
    def __init__(self):
        super().__init__("./images/bullet1.png",-3)



    def update(self):
        super().update()

        if self.rect.bottom<0:
            self.kill()

