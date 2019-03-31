#!/usr/local/bin python
# -*- coding:utf-8 -*-

import uiautomator2 as u2
from time import sleep

d = u2.connect('ce27dc09')

# 启动App
d.app_start("com.netease.snailread")
sleep(5)#等待日报弹窗出现

d(resourceId="com.netease.snailread:id/daily_close").click()#关闭弹窗

# d.disable_popups(True) #自动关闭弹窗，官方：很不稳定

#邮箱账号登录
d(resourceId="com.netease.snailread:id/title", text=u"我").click()
d(resourceId="com.netease.snailread:id/tv_login_or_register").click()
d(resourceId="com.netease.snailread:id/btn_email_login").click()
d(resourceId="com.netease.snailread:id/tv_urs_account").set_text("wnlm01@163.com")
d(resourceId="com.netease.snailread:id/tv_urs_passwd").set_text("qa1234")
d(resourceId="com.netease.snailread:id/tv_urs_login").click()

#阅读书桌第一本书
d(resourceId="com.netease.snailread:id/title", text=u"书桌").click()
d(resourceId="com.netease.snailread:id/iv_book_cover").click()
sleep(3)#等待正文加载


#每秒上滑一次页面
for x in range(60):
    d.swipe(0.5,0.5,0.5,1)
    print(x+1)
    sleep(1)

#退出登录，为下次测试做准备
d.press("back")
d(resourceId="com.netease.snailread:id/title", text=u"我").click()
d.swipe(0.5,0.5,0.5,1)
d(text=u"设置").click()
d.swipe(0.5,0.5,0.5,1)
d(resourceId="com.netease.snailread:id/tv_logout").click()
d(resourceId="com.netease.snailread:id/dialog_sr_right").click()

#退出应用
for x in range(5):
    d.press("back")
    sleep(0.5)
# 停止app
# d.app_stop("com.netease.snailread")