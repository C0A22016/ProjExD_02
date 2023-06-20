import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
key_dct = {
    pg.K_UP:(0,-5),
    pg.K_DOWN: (0,+5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(+5,0)
    }


def in_Judge(r): 
    """
    こうかとんrect,爆弾rectが画面外 or 画面内かを判定する関数
    引数：こうかとんrect or 爆弾rect
    戻り値：横方向、縦報告の判定結果タプル(True:画面内、False:画面外)

    """
    onw, onh = True, True
    if r.left < 0 or WIDTH < r.right:
        onw = False 
    if r.top < 0 or HEIGHT < r.bottom:
        onh *= False
    return  onw, onh

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    kk_rect.center = 900, 400
    # こうかとんsurfaceからこうかとんrectを抽出
    bd_img = pg.Surface((20, 20))  # 練習1
    bd_img.set_colorkey((0, 0, 0)) # surfaceを透明に
    pg.draw.circle(bd_img, (255, 0, 0), (10,10), 10)
    x = random.randint(0,WIDTH)
    y = random.randint(0, HEIGHT)
    bd_rect = bd_img.get_rect()
    # 爆弾surfaceから爆弾rectを抽出する
    bd_rect.center = x, y  
    # 爆弾rectの中心座標を乱数で指定する
    clock = pg.time.Clock()
    tmr = 0
    vx, vy = +5, +5
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        key_lst = pg.key.get_pressed()  # 練習3
        sum_mv = [0, 0]
        past_rect = kk_rect
        for k ,v in key_dct.items():
            if key_lst[k]:
                 sum_mv[0] += v[0]
                 sum_mv[1] += v[1]   
        kk_rect.move_ip(sum_mv[0], sum_mv[1])
        if in_Judge(kk_rect) != (True, True):
            kk_rect.move_ip(-sum_mv[0], -sum_mv[1])
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)  
        bd_rect.move_ip(vx, vy)  # 練習2
        bd_x, bd_y = in_Judge(bd_rect)
        if not bd_x:
            vx *= -1
        if not bd_y:
            vy *= -1 
        screen.blit(bd_img, bd_rect)
        pg.display.update()
        tmr += 1
        
        
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()