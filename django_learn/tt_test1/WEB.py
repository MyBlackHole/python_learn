import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.select import Select


def adminlogin(driver, myadmin, pwd):
    """登陆"""
    driver.get("http://127.0.0.1/admin")
    username = driver.find_element_by_name('username')
    username.send_keys(myadmin)
    time.sleep(1)
    username = driver.find_element_by_name('password')
    username.send_keys(pwd)
    time.sleep(1)
    register = driver.find_element_by_css_selector("#login-form div.submit-row > input")
    register.click()


def addtype(driver, myname, myname1, id):
    """添加种类"""
    type = driver.find_element_by_link_text(myname)
    time.sleep(2)
    type.click()
    addtypes = driver.find_element_by_link_text('增加 ' + myname)
    time.sleep(2)
    addtypes.click()

    # 种类参数输入
    name = driver.find_element_by_name('name')
    name.send_keys(myname1)
    time.sleep(1)
    image = driver.find_element_by_name('image')
    image.send_keys("/home/black/PycharmProjects/浏览器自动化/ceshi.jpeg")
    time.sleep(2)
    if id == 1:
        select = Select(driver.find_element_by_id("id_type"))
        select.select_by_visible_text(u"测试种类")
        time.sleep(2)
        driver.switch_to.frame('id_detail_ifr')
        body_string = """
        测试文本！
        富文本输入测试！
        输入成功！
        """
        driver.find_element_by_tag_name('body').send_keys(body_string)
        time.sleep(2)
    else:
        logo = driver.find_element_by_name('logo')
        logo.send_keys("测试标识")
    driver.switch_to.default_content()
    save = driver.find_element_by_name('_save')
    save.click()
    time.sleep(1)


def login(driver, userceshi):
    """登陆"""
    driver.get("http://127.0.0.1/user/login")
    username = driver.find_element_by_name('username')
    username.send_keys(userceshi)
    time.sleep(2)
    username = driver.find_element_by_name('pwd')
    username.send_keys("1358244533")
    time.sleep(2)
    register = driver.find_element_by_css_selector("#c_form-h button.btn.bg-primary")
    register.click()
    time.sleep(1)


def cart(driver):
    """添加到购物车"""
    # 首页商品点击添加到购物车购物车
    register = driver.find_element_by_css_selector("div>div>div.row>div.col-lg-3.col-6.p-3>a")
    register.click()
    time.sleep(1)
    register = driver.find_element_by_id("add_cart")
    register.click()
    # time.sleep(5)
    while True:
        try:
            driver.switch_to.alert.accept()
            break
        except NoAlertPresentException:
            print("捕获异常继续循环")

    register = driver.find_element_by_css_selector("#navbar18 ul > li.nav-item:nth-child(4) > a.nav-link.text-white")
    register.click()
    time.sleep(1)


def register(driver1, is_merchant, name):
    """注册"""
    driver1.get("http://127.0.0.1")
    register = driver1.find_element_by_link_text('注册')
    time.sleep(2)
    register.click()
    username = driver1.find_element_by_name('user_name')
    username.send_keys(name)
    time.sleep(1)
    pwd = driver1.find_element_by_name('pwd')
    pwd.send_keys("1358244533")
    time.sleep(1)
    cpwd = driver1.find_element_by_name('cpwd')
    cpwd.send_keys("1358244533")
    time.sleep(1)
    email = driver1.find_element_by_name('email')
    email.send_keys("1358244533@qq.com")
    time.sleep(1)
    if is_merchant == 1:
        driver1.find_element_by_name('remember').click()
        time.sleep(2)

    register = driver1.find_element_by_css_selector("div>form>button.btn.btn-primary")
    print(register.text)
    register.click()
    print("请输入激活确认：")
    is_active = input()
    if is_active != "ok":
        sys.exit(0)
    time.sleep(4)


def addgoodssku(driver, myname, myname1):
    """添加sku"""
    type = driver.find_element_by_link_text(myname)
    time.sleep(3)
    type.click()
    addtypes = driver.find_element_by_link_text('增加 ' + myname)
    time.sleep(3)
    addtypes.click()

    # SKU参数输入
    select = Select(driver.find_element_by_id("id_goods"))
    select.select_by_visible_text(u"测试SPU")
    time.sleep(5)
    name = driver.find_element_by_name('name')
    name.send_keys(myname1)
    desc = driver.find_element_by_name('desc')
    desc.send_keys("测试商品")
    time.sleep(3)
    price = driver.find_element_by_name('price')
    price.send_keys("600")
    time.sleep(3)
    unite = driver.find_element_by_name('unite')
    unite.send_keys("1")
    time.sleep(3)
    stock = driver.find_element_by_name('stock')
    stock.send_keys("4000")
    time.sleep(3)
    image = driver.find_element_by_name('image')
    image.send_keys("/home/black/PycharmProjects/浏览器自动化/ceshi.jpeg")
    time.sleep(3)
    save = driver.find_element_by_name('_save')
    save.click()
    time.sleep(1)


def admin():
    """admin添加种类操作"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    adminlogin(driver, "admin", "1358244533")
    time.sleep(2)
    addtype(driver, "商品种类", "测试种类", 0)
    time.sleep(3)
    driver.close()


def address(driver):
    receiver = driver.find_element_by_id("receiver")
    receiver.send_keys("ceshi")
    time.sleep(1)
    phone = driver.find_element_by_id("phone")
    phone.send_keys("15077459464")
    time.sleep(1)
    addr = driver.find_element_by_id("addr")
    addr.send_keys("测试某地点")
    time.sleep(1)
    zip_code = driver.find_element_by_id("zip_code")
    zip_code.send_keys("543100")
    time.sleep(1)
    tjdz = driver.find_element_by_id("tjdz")
    tjdz.click()
    while True:
        try:
            driver.switch_to.alert.accept()
            break
        except NoAlertPresentException:
            print("捕获异常继续循环")
    time.sleep(1)


# admin种类添加
admin()

option1 = webdriver.ChromeOptions()
option1.add_argument(r"user-data-dir=/home/black/PycharmProjects/浏览器自动化/merchant")

# 商家
merchantceshi = webdriver.Chrome(options=option1)
merchantceshi.maximize_window()
register(merchantceshi, 1, "merchantceshi")
time.sleep(1)
adminlogin(merchantceshi, "merchantceshi", "1358244533")
time.sleep(1)
addtype(merchantceshi, "商品SPU", "测试SPU", 1)
time.sleep(1)
addtypes = merchantceshi.find_element_by_link_text('首页')
time.sleep(2)
addtypes.click()
addgoodssku(merchantceshi, "商品", "测试SKU")
time.sleep(2)
addtypes = merchantceshi.find_element_by_link_text('查看站点')
time.sleep(2)
addtypes.click()
# merchantceshi.close()

# 用户
option = webdriver.ChromeOptions()
option.add_argument(r"user-data-dir=/home/black/PycharmProjects/浏览器自动化/user")
userceshi = webdriver.Chrome(options=option)
userceshi.maximize_window()
register(userceshi, 0, "userceshi")
time.sleep(2)
login(userceshi, "userceshi")
time.sleep(1)
cart(userceshi)
time.sleep(2)

# 订单结算
checkbox_all = userceshi.find_element_by_name('checkbox_all')
checkbox_all.click()
time.sleep(2)
jiesuan = userceshi.find_element_by_id("jiesuan")
jiesuan.click()
time.sleep(2)

# 地址添加
addtypes = userceshi.find_element_by_link_text('编辑地址')
time.sleep(2)
addtypes.click()
address(userceshi)
time.sleep(2)

# 回退网页
userceshi.back()
time.sleep(2)

# 刷新
userceshi.refresh()
time.sleep(2)

# 确认订单
jiesuan = userceshi.find_element_by_id("queren")
jiesuan.click()
time.sleep(2)
while True:
    try:
        userceshi.switch_to.alert.accept()
        break
    except NoAlertPresentException:
        print("捕获异常继续循环")
# userceshi.close()


# 订单逻辑
userstatus = userceshi.find_element_by_css_selector(
    "#tabtwo div.card.text-white.bg-primary.mb-2.pi-draggable > div.card-header > div.row.pi-draggable > div.col-md-4 > div.btn.btn-danger.status")
print(userstatus.text)
userstatus.click()
time.sleep(2)
while True:
    try:
        userceshi.switch_to.alert.accept()
        break
    except NoAlertPresentException:
        print("捕获异常继续循环")
# 商家
merchantceshi.maximize_window()
addtypes = merchantceshi.find_element_by_link_text('用户中心')
time.sleep(2)
addtypes.click()
merchantceshi.get("http://127.0.0.1/user/order/merchant/1")
time.sleep(2)
merchantstatus = merchantceshi.find_element_by_css_selector(
    "#tabtwo div.card.text-white.bg-primary.mb-2.pi-draggable:first-child > div.row.pi-draggable > div.col-md-12 > div.row.pi-draggable.pb-1 > div.col-md-2.px-0.order_status")
print(merchantstatus.text)
merchantstatus.click()
time.sleep(2)
while True:
    try:
        merchantceshi.switch_to.alert.accept()
        break
    except NoAlertPresentException:
        print("捕获异常继续循环")

# 用户
userceshi.maximize_window()
userceshi.refresh()
time.sleep(2)
userstatus = userceshi.find_element_by_css_selector(
    "#tabtwo div.card.text-white.bg-primary.mb-2.pi-draggable> div.row.pi-draggable> div.col-md-12 > div.row.pi-draggable.pb-1 > div.col-md-2.px-0.order_status")
print(userstatus.text)
userstatus.click()
time.sleep(2)
while True:
    try:
        userceshi.switch_to.alert.accept()
        break
    except NoAlertPresentException:
        print("捕获异常继续循环")
# userceshi

time.sleep(2)
userceshi.refresh()
userstatus = userceshi.find_element_by_css_selector(
    "#tabtwo div.card.text-white.bg-primary.mb-2.pi-draggable:first-child > div.row.pi-draggable:last-child > div.col-md-12 > div.row.pi-draggable.pb-1 > div.col-md-2.px-0.order_status")
print(userstatus.text)
userstatus.click()
time.sleep(2)
# while True:
#     try:
#         userceshi.switch_to.alert.accept()
#         break
#     except NoAlertPresentException:
#         print("捕获异常继续循环")
time.sleep(3)
jiesuan = userceshi.find_element_by_id("form35")
time.sleep(2)
jiesuan.send_keys("测试结束!!!")
time.sleep(2)

userstatus = userceshi.find_element_by_css_selector("button.btn.btn-outline-danger.btn-block.active")
print(userstatus.text)
userstatus.click()
time.sleep(2)

# 商家
merchantceshi.maximize_window()
merchantceshi.refresh()
