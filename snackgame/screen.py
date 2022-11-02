from random import randint
import sys
import pygame as pg
from sprite import SnackBody,SnackHead,Food 


FPS=5   #调整游戏速度
screen_size = (500,500)  #调整游戏画面尺寸


pg.init()
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Snack")
snack_head=SnackHead('resource/snack_head.jpg',(100,100))
snack_group = pg.sprite.Group()
snack_list=[]
snack_list.append(snack_head)
food=Food('resource/food.jpg',(200,200))


font=pg.font.Font('resource/STKAITI.TTF',50)
text=font.render("游戏结束",True,(0,0,255),(0,255,0))
PositionText=text.get_rect()

key_flag=0
game_over=0
clock = pg.time.Clock()

pg.display.set_caption("黄猛")
while True:
    clock.tick(FPS)
    if game_over == 0:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                key_flag=event
        if key_flag != 0:
            snack_head.rect = snack_head.GetRect(key_flag)

        for i in range(1,len(snack_list)):
            snack_list[i].BeforePosition = snack_list[i].rect
            snack_list[i].rect = snack_list[i-1].GetBeforePosition()

        if pg.sprite.collide_rect(snack_head,food):
            food.rect.topleft = (randint(0,screen_size[0]-food.image.get_size()[0]),randint(0,screen_size[1]-food.image.get_size()[1]))
            while pg.sprite.collide_rect(food,snack_head) or pg.sprite.spritecollideany(food,snack_group):
                food.rect.topleft = (randint(0,screen_size[0]-food.image.get_size()[0]),randint(0,screen_size[1]-food.image.get_size()[1]))
            snack_body = SnackBody('resource/snack.png',snack_list[-1].GetBeforePosition().topleft)
            snack_group.add(snack_body)
            snack_list.append(snack_body)
        


    
    screen.fill('white')
    for s in snack_list:
        screen.blit(s.image,s.rect)
    screen.blit(food.image,food.rect)
    if snack_head.rect[0] < 0 or snack_head.rect[1] < 0 or snack_head.rect[0] > screen_size[0]-snack_head.image.get_size()[0] or snack_head.rect[1] > screen_size[1]-snack_head.image.get_size()[1] \
        or pg.sprite.spritecollideany(snack_head,snack_group):
        game_over = 1
    if game_over == 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        screen.blit(text,PositionText)
    screen.blit(snack_head.image,snack_head.rect)
    pg.display.flip()
