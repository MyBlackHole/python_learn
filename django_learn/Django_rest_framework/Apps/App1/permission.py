# 权限

class SVIPPremission(object):
    # 没有权限提示
    message = "必须是SVIP才能访问"

    def has_permission(self, request, view):
        if request.user.user_type != 3:
            return False
        return True


class MyPremission(object):
    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return False
        return True
