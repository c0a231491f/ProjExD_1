import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_g = pg.transform.flip(bg_img, True, False) #背景画像の左右反転
    kpg3 = pg.image.load("fig/3.png") #こうかとん読み込み
    kpg3 = pg.transform.flip(kpg3, True, False) #こうかとん左右反転
    kpg3_rect = kpg3.get_rect() #こうかとんのrectの取得
    kpg3_rect.center = 300, 200 #初期座標300，200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr%3200) #背景画像のX座標
        screen.blit(bg_img, [x, 0]) #右から左に動く背景画像
        screen.blit(bg_img_g, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0]) 
        screen.blit(bg_img_g, [x+4800, 0])

        key_lst =pg.key.get_pressed() #矢印キーを押した状態での移動
        if key_lst[pg.K_UP]:
            kpg3_rect.move_ip((0, -1)) #上
        if key_lst[pg.K_DOWN]:
            kpg3_rect.move_ip((0, 1)) #下
        if key_lst[pg.K_LEFT]:
            kpg3_rect.move_ip((-1, 0)) #左
        if key_lst[pg.K_RIGHT]:
            kpg3_rect.move_ip((1, 0)) #右
        screen.blit(kpg3, kpg3_rect) #こうかとん貼り付け

        pg.display.update()
        tmr += 1        
        clock.tick(200) #FPS200


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()