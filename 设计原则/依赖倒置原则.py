from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):

    @abstractmethod
    def pay(self):
        pass


class AliPay(Payment):
    def __init__(self):
        self.name = "支付宝"

    def pay(self):
        print(self.name)


class WeiCht(Payment):
    def __init__(self):
        self.name = "微信"

    def pay(self):
        print(self.name)


def run_pay(app):
    app.pay()


# run_pay(AliPay())
# run_pay(WeiCht())
d = {
    1: AliPay(),
    2: WeiCht()
}

run_type = 1
if run_type == 1:
    AliPay().pay()
elif run_type == 2:
    WeiCht().pay()

run_pay(d[1])
