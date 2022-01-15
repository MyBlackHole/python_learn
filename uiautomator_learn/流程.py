#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   流程
Description:
Author:      Black Hole
date:        2021/03/16 09:53:20:

-------------------------------------------------
Change Activity:
             2021/03/16 09:53:20:
-------------------------------------------------
"""


import time
from uiautomator import Device, device

# 连接设备
# d = Device('cae5ef26')
d = Device('710KPMZ0361243')

print(d.info)

# # 按home键
# d.press.home()


# d(text='微信').click()

# d(text='登陆').click()

# d(text='用微信号/QQ号/邮箱登陆').click()

# # 清空
# d.clear_text()
# d(text='请填写微信号/QQ号/邮箱').click()
# d.send_keys("你好123abcEFG") 

# 搜索符号
d(className="android.widget.ImageView", resourceId="com.tencent.mm:id/he6").wait.exists(timeout=4000)
d(className="android.widget.ImageView", resourceId="com.tencent.mm:id/he6").click()

# time.sleep(3)
d(text='公众号').wait.exists(timeout=4000)
status = d(text='公众号').click()
# 微信公众号
if status:

# time.sleep(3)

# d(text='搜索公众号').set_text('视频')

    time.sleep(3)
    d(index=2, resourceId="com.tencent.mm:id/bxz").wait.exists(timeout=4000)
    d(index=2, resourceId="com.tencent.mm:id/bxz").set_text('视频')
# d(text='搜索').set_text('视频')


# d(text='搜索').click()

# # d(className="android.widget.Button", resourceId="com.tencent.mm:id/hi4").click()

# # 输入检索文字
# d(text='搜索公众号').set_text('视频')

# d.set_fastinput_ime(False) # 切换成正常的输入法
# d.send_action("search") # 模拟输入法的搜索（很实用）
    d.press('enter')

# time.sleep(3)
