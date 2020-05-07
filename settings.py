class Settings():
    # 存储游戏的所有设置
    def __init__(self):
        # 屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        # 小人的设置
        self.man_speed_factor=1.5
        self.huluobo_speed_factor=0.2

        # 水果蔬菜设置
        self.HULUOBO='images/huluobo.bmp'
        self.DABAICAI='images/dabaicai.bmp'
        self.TUDOU='images/tudou.bmp'
        self.XIHONGSHI='images/xihongshi.bmp'
        self.LAJIAO='images/lajiao.bmp'
        self.NANGUA='images/nangua.bmp'
        self.XIANGJIAO='images/xiangjiao.bmp'
        self.PINGGUO='images/pingguo.bmp'
        self.ZHUANSHI='images/zhuanshi.bmp'
        self.XIGUA='images/xigua.bmp'
        self.WUPING=[self.HULUOBO,self.DABAICAI,self.TUDOU,self.XIHONGSHI,self.LAJIAO,
                     self.NANGUA,self.XIANGJIAO,self.PINGGUO,self.ZHUANSHI,self.XIGUA]



