import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    pg3 = pg.image.load("fig/3.png") #こうかとん読み込み
    pg3 = pg.transform.flip(pg3, True, False) #こうかとん左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%800
        screen.blit(bg_img, [-x, 0]) #右から左に動く
        screen.blit(pg3, [300, 200]) #こうかとん貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200) #FPS200


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()