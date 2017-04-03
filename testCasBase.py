# coding=utf-8
import os
from conf.globalFacts import  *
import unittest
from time import sleep

from appium import webdriver


#from juzhen import  *

from siftxy import *
from start2tingyuan import  *
from senceCheck import  *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):

    def yu_hun(self,type='yuhun',count = 3):
        starttime = time.time()
        #每一个count给5min，就是300s
        presettime = 300*count
        type = yunHunPath

        self.shot_screen()

        #点击御魂入口
        loggerInner.info("------click yu hun entry!! ")
        self.driver.tap([(int(XMAX*16/100),int(YMAX*95/100))])


        sleep(3)
        loggerInner.info("------click big snack at {x},{y}!! ".format(x=XMAX/4,y=YMAX/2))
        self.driver.tap([(XMAX/4,YMAX/2)])

        sleep(3)
        #点击挑战button
        loggerInner.info("------click yu hun fight entry button at {x},{y}!! ".format(x=int(XMAX*3/4),y=int(YMAX*7/10)))
        self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])



        while count >= 1:
            loggerInner.info("------now count={count}，that means {count} times should be tried again!! ".format(count=count))
            timenow = time.time()
            if (timenow - starttime)> presettime:
                break
            sleep(3)
            #点击挑战按钮
            loggerInner.info("------now count={count}，click fight start entry button  at {x},{y}!! ".format(count=count,x=int(XMAX*3/4),y=int(YMAX*7/10)))
            self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
            #点击开始战斗
            loggerInner.info("------now count={count}，click fight begin button  at {x},{y}!! ".format(count=count,x=int(XMAX*9/10),y=int(YMAX*8/10)))
            sleep(3)
            self.driver.tap([(int(XMAX*9/10),int(YMAX*8/10))])
            sences =  [

        {"sence": SenceTanSuoFuBenFighting, "path": SenceFlagTanSuoFuBenFightingPic},

        {"sence": SenceVictory, "path": SenceFlagSenceVictory},
        {"sence": SenceVictoryDaMo, "path": SenceFlagVictoryDaMo},

    ]
            self.shot_screen()
            sence = get_sence(defaultSSPath,sences=sences)
            if sence == SenceTanSuoFuBenFighting:
                #探测到当前在战斗画面，则每隔3s点击下中间屏幕即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == "otherSence":
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == SenceVictory:
                #探测到战斗成页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1
            elif sence == SenceVictoryDaMo:
                #探测到领取奖励页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1

    def jue_xing(self,type="lei",count=3):

        self.shot_screen()
        #点击觉醒入口
        self.driver.tap([(int(XMAX*8/100),int(YMAX*93/100))])
        #选择任意一个麒麟
        sleep(3)
        if type=="huo":
            self.driver.tap([(XMAX/5,YMAX/2)])
        if type=="feng":
            self.driver.tap([(XMAX*2/5,YMAX/2)])
        if type=="shui":
            self.driver.tap([(XMAX*3/5,YMAX/2)])
        if type=="lei":
            self.driver.tap([(XMAX*4/5,YMAX/2)])

        sleep(3)
        self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
        starttime = time.time()
        #每一个count给5min，就是300s
        presettime = 300*count



        while count >= 1:
            timenow = time.time()
            if (timenow - starttime)> presettime:
                break
            sleep(3)
            #点击挑战按钮
            self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
            #点击开始战斗
            sleep(3)
            self.driver.tap([(int(XMAX*9/10),int(YMAX*8/10))])
            sences =  [

        {"sence": SenceTanSuoFuBenFighting, "path": SenceFlagTanSuoFuBenFightingPic},

        {"sence": SenceVictory, "path": SenceFlagSenceVictory},
        {"sence": SenceVictoryDaMo, "path": SenceFlagVictoryDaMo},

    ]

            self.shot_screen()
            sence = get_sence(defaultSSPath,sences=sences)
            if sence == SenceTanSuoFuBenFighting:
                #探测到当前在战斗画面，则每隔3s点击下中间屏幕即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == "otherSence":
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == SenceVictory:
                #探测到战斗成页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1
            elif sence == SenceVictoryDaMo:
                #探测到领取奖励页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1

    def shot_screen_backup(self):
        #这个函数截取出来的图片是横屏的图片
        #sleep(1)
        self.driver.get_screenshot_as_file("screenshotPre.png")

        img = Image.open("screenshotPre.png")
        img2 = img.transpose(Image.ROTATE_270)
        img2.save(defaultSSPath)
    def shot_screen(self):
        #这个函数截图出来的图片是竖屏的图片，为了保证响应速度，我们使用这个函数来配合图片识别操作的函数（也就是siftxy.py里面的函数，对应的x,y返回结果时，我们也做了相关的线性变化）
        #sleep(1)
        self.driver.get_screenshot_as_file(defaultSSPath)

    def tan_suo(self,count=1,level=tanSuoLevel13Path):
        starttime = time.time()
        #每一个count给15min，就是900s
        presettime = 900*count



        self.shot_screen()
        if level == "level10":
            level = tanSuoLevel10Path
        if level == "level11":
            level = tanSuoLevel13Path

        x,y = get_x_y(defaultSSPath,level)
        loggerInner.info("------get fight level  at {x},{y} ".format(x=x,y=y))
        self.driver.tap([(x,y)])
        sleep(6)
        #点击探索button，进入选择小怪页面
        loggerInner.info("------click level fight entry button at {x},{y} ".format(x=int(XMAX*3/4),y=int(YMAX*7/10)))
        self.shot_screen()
        self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
        sleep(6)

        self.shot_screen()


        #我们一共需要打三次副本

        step = 0
        direction = 1
        while count >= 0:
            timenow = time.time()
            if (timenow - starttime)> presettime:
                break
            self.shot_screen()
            sence = get_sence(defaultSSPath)
            loggerInner.info("------now sence is {sence}".format(sence=sence))
            if sence == SenceTanSuoFuBenXuanZe:
                #只进行妖怪打斗标志检索，检索完了点击。如果检索不到就往右移动半屏幕(四次之后改变方向移动四次)，再次检索。
                self.shot_screen()
                x,y = get_x_y(defaultSSPath,SenceBossFightPic)
                if x != "nox":
                    loggerInner.info("------find boss,at {x},{y}".format(x=x,y=y))
                    self.driver.tap([(x,y)])

                self.shot_screen()
                x,y = get_x_y(defaultSSPath,tanSuoZhunBeiPath)
                if x != "nox":
                    loggerInner.info("------find an small demo,at {x},{y}".format(x=x,y=y))
                    self.driver.tap([(x,y)])
                    sleep(3)

                else:
                    #没找到妖怪的话有可能是发现大boss了（或者打完boss掉落好东西了），也有可能真的没发现任何人，我们就要走两步了去找妖怪去
                    #判断如果有boss，就打boss
                    self.shot_screen()

                    x,y = get_x_y(defaultSSPath,bossJiangpinButton)
                    if x != "nox":
                        loggerInner.info("------after boss fight ,there is some trasures,at {x},{y}".format(x=x,y=y))
                        self.driver.tap([(x,y)])
                    step = direction + step
                    if step > 0:
                        loggerInner.info("------step right forward")
                        self.driver.tap([(XMAX-1,int(YMAX*4/5))])
                        sleep(6)
                        if step >= 4:
                            step = 0
                            direction = -direction
                    elif step < 0:
                        loggerInner.info("------step left forward")
                        self.driver.tap([(0,int(YMAX*4/5))])
                        sleep(6)
                        if step <= -4:
                            step = 0
                            direction = -direction




            elif sence == SenceTanSuoFuBenFighting:
                #探测到当前在战斗画面，则每隔3s点击下中间屏幕即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == "otherSence":
                x,y = get_x_y(defaultSSPath,level)
                if x != "nox":
                    loggerInner.info("------find level fight at {x},{y} ".format(x=x,y=y))

                    self.driver.tap([(x,y)])
                    sleep(6)



                x,y=get_x_y(defaultSSPath,fuBenTanSuoKaiShiButton,accurate=0.1)
                if x != "nox":
                    self.driver.tap([(x,y)])

                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == SenceVictory:
                loggerInner.info("------fight ends,receive your rewards!----")
                #探测到战斗成页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == SenceVictoryDaMo:
                loggerInner.info("------fight ends,receive your rewards!damo----")
                #探测到领取奖励页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])

            elif sence == SenceTanSuoFuBenHomePage:
                #探测到探索关卡选择页面，我们先找到需要打的关卡，进入后，点击开始探索按钮即可
                self.shot_screen()
                x,y = get_x_y(defaultSSPath,level)
                loggerInner.info("------get fight level at {x},{y}".format(x=x,y=y))
                self.driver.tap([(x,y)])
                sleep(3)
                self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
                sleep(3)
                count = count - 1

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '127.0.0.1:52001'
        desired_caps['appPackage'] = 'com.netease.onmyoji.huawei'
        desired_caps['appActivity'] = 'com.netease.onmyoji.Launcher'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    #######这里是最开始的几个测试用例，后来分离到了单个用例里面去了
    # def test_1_yu_hun(self):
    #     loggerInner.info("------start yu hun!! ")
    #     start2TingYuan(self.driver)
    #     #点击探索探索
    #     loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
    #     self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
    #     sleep(5)
    #     self.yu_hun(count=3)
    # def test_2_jue_xing(self):
    #     loggerInner.info("------start jue xing !!")
    #     start2TingYuan(self.driver)
    #     #点击探索探索
    #     loggerInner.info("------click search button in tingyuan at {x},{y}".format(x=int(XMAX*53/100),y=int(YMAX/5)))
    #     self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
    #     sleep(5)
    #     self.jue_xing(type='shui',count=3)
    # def test_3_tan_suo_fu_ben(self):
    #     loggerInner.info("------start level fight tasks !!")
    #     start2TingYuan(self.driver)
    #     #点击探索探索
    #     loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
    #     self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
    #     sleep(5)
    #     self.tan_suo(count=3)












if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
