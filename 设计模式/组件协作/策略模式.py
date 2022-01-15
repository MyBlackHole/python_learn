#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Customer:
    def __init__(self):
        self.customer_name = ""
        self.snd_way = ""
        self.info = ""
        self.phone = ""
        self.email = ""

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, mail):
        self.email = mail

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def set_info(self, info):
        self.info = info

    def set_name(self, name):
        self.customer_name = name

    def set_brd_way(self, snd_way):
        self.snd_way = snd_way

    def snd_msg(self):
        self.snd_way.send(self.info)


class MsgSender(metaclass=ABCMeta):
    def __init__(self):
        self.dst_code = ""

    def set_code(self, code):
        self.dst_code = code

    @abstractmethod
    def send(self, info):
        pass


class EmailSender(MsgSender):
    def send(self, info):
        print("EMAIL_ADDRESS:%s EMAIL:%s" % (self.dst_code, info))


class TextSender(MsgSender):
    def send(self, info):
        print("TEXT_CODE:%s EMAIL:%s" % (self.dst_code, info))


if __name__ == "__main__":
    customer_x = Customer()
    customer_x.set_name("CUSTOMER_X")
    customer_x.set_phone("10023456789")
    customer_x.set_email("customer_x@xmail.com")
    customer_x.set_info("Welcome to our new party!")
    text_sender = TextSender()
    text_sender.set_code(customer_x.get_phone())
    customer_x.set_brd_way(text_sender)
    customer_x.snd_msg()
    mail_sender = EmailSender()
    mail_sender.set_code(customer_x.get_email())
    customer_x.set_brd_way(mail_sender)
    customer_x.snd_msg()
