#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod


class Abstract:
    @abstractmethod
    def __init__(self):
        self.mid = ""
        self.name = ""

    def get_name(self):
        print("A protocol getName method...id:%s" % self.mid)
        return self.name

    def set_name(self, name):
        print("A protocol setName method...id:%s" % self.mid)
        self.name = name


class ACpnStaff(Abstract):
    """
    A公司
    """

    def __init__(self, mid):
        super().__init__()
        self.mid = mid
        self.name = ""
        self.phone = ""

    def get_phone(self):
        print("A protocol getPhone method...id:%s" % self.mid)
        return self.phone

    def set_phone(self, phone):
        print("A protocol setPhone method...id:%s" % self.mid)
        self.phone = phone


class BCpnStaff(Abstract):
    """
    公司
    """

    def __init__(self, id):
        super().__init__()
        self.mid = ""
        self.telephone = ""

    def get_telephone(self):
        print("B protocol get_telephone method...id:%s" % self.mid)
        return self.telephone

    def set_telephone(self, telephone):
        print("B protocol get_name method...id:%s" % self.mid)
        self.telephone = telephone


class CpnStaffAdapter:
    """
    C公司
    """

    def __init__(self, mid):
        self.b_cpn = BCpnStaff(mid)

    def get_name(self):
        return self.b_cpn.get_name()

    def get_phone(self):
        return self.b_cpn.get_telephone()

    def set_name(self, name):
        self.b_cpn.set_name(name)

    def set_phone(self, phone):
        self.b_cpn.set_telephone(phone)


# 业务场景
if __name__ == "__main__":
    a_staff = ACpnStaff("123")
    a_staff.set_name("X-A")
    a_staff.set_phone("10012345678")
    print("A Staff Name:%s" % a_staff.get_name())
    print("A Staff Phone:%s" % a_staff.get_phone())
    b_staff = CpnStaffAdapter("456")
    b_staff.set_name("Y-B")
    b_staff.set_phone("99987654321")
    print("B Staff Name:%s" % b_staff.get_name())
    print("B Staff Phone:%s" % b_staff.get_phone())
