from typing import Text
import uiautomator2 as u2


d = u2.connect()

def login(d):
    """
    登录微信
    """
    # d(text='登录').click()
    d(resourceId="com.tencent.mm:id/erw").click()
    d(resourceId="com.tencent.mm:id/bxz", text="请填写微信号/QQ号/邮箱").set_text('15077459464')
    d(resourceId="com.tencent.mm:id/bxz", text="请填写密码").set_text('abc12345678')
    d(resourceId="com.tencent.mm:id/erp").click()
    print(d.info)


# d(resourceId="com.tencent.mm:id/he6").click()
# d(resourceId="com.tencent.mm:id/il4", text="公众号").click()
# # d(resourceId="com.tencent.mm:id/il4", text="公众号").click()
# d.dump()
# d(text="搜索公众号").set_text('视频')


def search_public():
    d(resourceId="com.tencent.mm:id/dub", text="通讯录").click()
    d(resourceId="com.tencent.mm:id/a99").click()
    d.xpath('//android.support.v7.widget.LinearLayoutCompat/android.widget.LinearLayout[1]').click()
    d.xpath('//*[@resource-id="com.tencent.mm:id/db_"]').set_text('视频')
    d.xpath('//*[@resource-id="com.tencent.mm:id/jkg"]').click()

    # d.set_fastinput_ime(True)
    # d.press('enter')
    # d.xpath('//*[@resource-id="com.google.android.inputmethod.pinyin:id/key_pos_ime_action"]/android.widget.ImageView[2]').click()

def attention(x, y):
    d.click(x, y)
    attention_status = d.exists(resourceId="com.tencent.mm:id/a5l", text='关注')
    if attention_status:
        d(resourceId="com.tencent.mm:id/a5l").click()
        d(resourceId="com.tencent.mm:id/un").click()
        d(resourceId="com.tencent.mm:id/ei").click()
        return "关注成功"
    else:
        return "已经关注"

# login(d)
# print(attention(x=0.4, y=0.2))

def attention_main():
    pass

if __name__ == "__main__":
    pass