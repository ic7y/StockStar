import random
import string
import hashlib
import base64


class UserService:
    # salt值生成
    @staticmethod
    def genSalt(length=16):
        keyList = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
        return "".join(keyList)

    # 服务器存储的密码生成
    @staticmethod
    def genPwd(pwd, salt):
        # 生成MD5对象
        MD5 = hashlib.md5()
        # 待加密字符串生成：base64过的密码+salt盐值
        clearText = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
        # MD5散列
        MD5.update(clearText.encode("utf-8"))
        # 返回散列的16进制值(32位)
        return MD5.hexdigest()

    # 生成cookie的value
    @staticmethod
    def genAuthCode(user_info=None):
        MD5 = hashlib.md5()
        clearText = "%s-%s-%s-%s-%s" % (
            user_info.id, user_info.login_name, user_info.login_password, user_info.login_salt, user_info.status)
        MD5.update(clearText.encode('utf-8'))
        return MD5.hexdigest()
