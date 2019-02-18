import pygame
import time
from plane_sprites import *
# 飞机爆炸效果没做

class PlaneGame(object):
    '''主游戏'''


    def __init__(self):
        print("游戏初始化")

        pygame.init()
        # 1 创建游戏窗口
        self.screen =  pygame.display.set_mode(SCREEN_RECT.size)
        # 创建标题
        pygame.display.set_caption("飞机大战")

        # 2 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3 调用私有方法 精灵和精灵组的创建
        self.__create_sprites()
        # 设置定时器事件 ：创建敌机 1s
        pygame.time.set_timer(CRESTR_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,400)

    def __create_sprites(self):

        # 创建背景精灵
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def startGame(self):
        print("游戏开始")

        while True:
            # 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 跟新/绘制精灵组
            self.__update_sprites()
            # 更新屏幕显示
            pygame.display.update()


    def __event_handler(self):
        # 事件监听
        for event in pygame.event.get():

            # 判断是否退出
            if event.type == pygame.QUIT:
                self.__game_over(self)
            elif event.type == CRESTR_ENEMY_EVENT:
                #print("敌机出厂")
                # 创建敌机 添加入组
                enemy = Enemy()
                self.enemy_group.add(enemy)
            # 事件监听模式只能单次按键
            # elif event.type==pygame.KEYDOWN:
            #     if event.key == pygame.K_RIGHT:
            #         print("右移")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0
    def __check_collide(self):

        # 子弹碰撞销毁
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)

        # 机撞机
        enemyies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemyies) > 0:
            # 英雄牺牲
            self.kill()

            # 游戏结束
           # PlaneGame.__game_over()

    def __update_sprites(self):
        # 背景
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 敌机
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 英雄
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 子弹
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.startGame()

    time.sleep(5)




