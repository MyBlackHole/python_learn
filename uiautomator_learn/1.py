#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   1
Description:
Author:      Black Hole
date:        2021/03/15 12:23:49:

-------------------------------------------------
Change Activity:
             2021/03/15 12:23:49:
-------------------------------------------------
"""

from uiautomator import Device


# 连接设备
d = Device('cae5ef26')

# # 打开屏幕
# d.screen.on()
# # 关闭屏幕
# d.screen.off()

# # 唤醒设备
# d.wakeup()

# # 休眠设备
# d.sleep()

# 按home键
d.press.home()
# print(d().info)

# 屏幕边缘下滑
# d().swipe.down(steps=10)
print(d.info['displayHeight'], d.info['displayWidth'])

# # 屏幕左滑
# d.swipe(800, 500, 50, 500, steps=10)

# # 屏幕右滑
# d.swipe(50, 500, 500, 500, steps=10)

# print(d(text="支付宝").info)

# # 按返回键
# d.press.back()
# d.press("left")
# home
# back
# left
# right
# home
# back
# left
# right
# up
# down
# center
# menu
# search
# enter
# delete(or del)
# recent(recent apps)
# volume_up
# volume_down
# volume_mute
# camera
# power


# #点击屏幕
# # click (x, y) on screen
# d.click(x, y)
# #长按屏幕
# # long click (x, y) on screen
# d.long_click(x, y)


# # 按下键码0×07（‘0’）与ALT （0X02） 
# d.press(0x07,0X02)


# # 屏幕截图
# d.screenshot("home.png")

# # 将当前屏幕结构保存在本机并命名为"heierarchy.xml"
# d.dump("hierarchy.xml")

# # 或者将存储值作为结果返回
# xml=d.dump()
# print(xml)


# # 打开通知消息栏，不能用于Android 4.3以前的版本 (mix异常)
# d.notification()

# # 打开快速设置栏，不能用于Android 4.3以前的版本
# d.open.quick_settings()
# xml=d.dump()
# print(xml)

# # 等待当前窗口空闲
# d.wait.idle()
# # 等待直到窗口发生刷新事件
# d.wait.update()


### 监视器
# d.watcher(name)
# （创建一个新的监视器，并将其命名为“name”）
#  .when(condition)
# # （为监视器添加添加一个Uiselector条件）
#  .click(target)
# （执行对目标Uiselector点击动作）
# （按顺序依次按下key）
# （定义另一种键值序列的方法是‘press(<keybname>, ..., <keyname>)’）
# .press("back", "home")


d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
                             .click(text="支付宝")


# （监视器被触发为‘真’，反之则为‘假’）
print(d.watcher("watcher_name").triggered)


# # （重置所有已触发的监视器，并且将d.watchers.triggered 参数变为false）
# d.watchers.reset()


# # （删除监视器）
# d.watcher("AUTO_FC_WHEN_ANR").remove()


# （一个已注册的监视器名称列表）
print(d.watchers)


# （删除所有已触发的监视器）
d.watchers.remove()

# # （删除特定名称的监视器，与d.watcher("watcher_name").remove() 相同）
# d.watchers.remove("watcher_name")


# # （强制运行所有已注册的监视器）
# d.watchers.run()



### 处理程序

# # （返回True来中断处理程序回调函数的循环）
# def fc_close(device):
#   if device(text='Force Close').exists:
#     device(text='Force Close').click()
#   return True  

# # （打开处理程序返回函数j
# d.handlers.on(fc_close)

# # （关闭处理程序返回函数）
# d.handlers.off(fc_close)

d(text='微信').click()

# # 获取当前窗口信息
# print(d.info)