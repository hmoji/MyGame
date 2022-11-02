from random import randint
import sys
from pygame.sprite import Sprite as sp
import pygame as pg
import queue



class Snack(sp):
    def __init__(self,filename:str,location:tuple,size:tuple[int,int]=(50,50)):
        # 调父类来初始化子类
        sp.__init__(self)
        # 加载图片
        self.image = pg.transform.scale(pg.image.load(filename).convert(),size)
        # 获取图片rect区域
        self.rect = self.image.get_rect()
        # 获取图片尺寸
        self.image_size = self.image.get_size()
        # 设置位置
        self.rect.topleft = location
        # 每帧移动的像素
        self.shift_pixel = self.image_size[0]

        self.BeforePosition=self.rect

        self.PositionQueue = queue.Queue(1)
        self.PositionQueue.put(self.rect)

    def Copy(self):
        return Snack(self.image,self.rect.topleft)

    def GetRect(self,press):
        self.__PressCheck()
        return self.__Press(press)

    

    def __PressCheck(self):
        if self.PositionQueue.full():
            self.BeforePosition = self.PositionQueue.get()


    def __Press(self,press):
        if press.key == pg.K_UP:
            move_rect = self.rect.move(self.__UP())
            self.PositionQueue.put(move_rect)
            return move_rect

        if press.key == pg.K_DOWN:
            move_rect = self.rect.move(self.__DOWN())
            self.PositionQueue.put(move_rect)
            return move_rect
        
        if press.key == pg.K_LEFT:
            move_rect = self.rect.move(self.__LEFT())
            self.PositionQueue.put(move_rect)
            return move_rect

        if press.key == pg.K_RIGHT:
            move_rect = self.rect.move(self.__RIGHT())
            self.PositionQueue.put(move_rect)
            return move_rect
    
    def __UP(self):
        return (0,-self.shift_pixel)
    
    def __DOWN(self):
        return (0,self.shift_pixel)
    
    def __LEFT(self):
        return (-self.shift_pixel,0)
    
    def __RIGHT(self):
        return (self.shift_pixel,0)

    def GetBeforePosition(self):
        return self.BeforePosition

class SnackHead(Snack):
    def __init__(self,filename:str,location:tuple,size:tuple[int,int]=(50,50)):
        # 调父类来初始化子类
        Snack.__init__(self,filename,location)
        # self.rect = self.image.get_rect()

class SnackBody(sp):
    def __init__(self,filename:str,location:tuple,size:tuple[int,int]=(50,50)):
        # 调父类来初始化子类
        sp.__init__(self)
        # 加载图片
        self.image = pg.transform.scale(pg.image.load(filename).convert(),size)
        # 获取图片rect区域
        self.rect = self.image.get_rect()
        # 设置位置
        self.rect.topleft = location

        self.BeforePosition=self.rect

    def GetBeforePosition(self):
        # print(self.BeforePosition)
        return self.BeforePosition



        

class Food(sp):
    def __init__(self,filename:str,location:tuple):
        # 调父类来初始化子类
        sp.__init__(self)
        # 加载图片
        self.image = pg.transform.scale(pg.image.load(filename).convert(),(50,50))
        # 获取图片rect区域
        self.rect = self.image.get_rect()
        # 设置位置
        self.rect.topleft = location
