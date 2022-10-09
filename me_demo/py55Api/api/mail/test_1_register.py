# -*- coding:utf-8 -*-
import requests
import faker
import pymysql


class MemberRegister:
    def __init__(self):
        self.fk = faker.Faker("zh-cn")  # 初始化造数据方法
        self.mobile = self.fk.phone_number()
        print("随机生成的手机号是：", self.mobile)
        self.db = pymysql.connect(host="47.113.180.81",
                                  port=3306,
                                  user="lemon",
                                  password="lemon123",
                                  db="yami_shops",
                                  autocommit=True,
                                  cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()  # 游标
        self.send_msg_url = "http://mall.lemonban.com:8107/user/sendRegisterSms"
        self.check_msg_code_url = "http://mall.lemonban.com:8107/user/checkRegisterSms"
        self.user_register_url = "http://mall.lemonban.com:8107/user/registerOrBindUser"

    # 发送短信接口(请求我们后端，让后端把调用第三方发短信，建议测试环境把发送短信功能去掉)
    def send_msg(self):
        data = {
            "mobile": self.mobile
        }
        res = requests.put(url=self.send_msg_url, json=data)
        print("发送的验证码是：", res.text)

    # 校验短信验证码是否正确，返回字符串
    def check_msg_code(self):
        # self.send_msg()
        sql = "SELECT mobile_code FROM tz_sms_log where user_phone = '{}' ORDER BY id DESC".format(self.mobile)
        self.cur.execute(sql)  # 游标操作
        # 取出查询后的值,因为返回的是一个list，所以要通过索引取值
        # 短信验证码为： [{'mobile_code': '667744'}]
        msg_code = self.cur.fetchall()[0]
        print("短信验证码为：", msg_code)
        data = {
            "mobile": self.mobile,
            "validCode": msg_code["mobile_code"]  # 参数化
        }
        res = requests.put(url=self.check_msg_code_url, json=data)
        print("校验短信返回：", res.text)
        return res.text

    # 注册用户
    def user_register(self):
        self.send_msg()
        msg_code = self.check_msg_code()
        data = {
            "appType": 3,
            "checkRegisterSmsFlag": msg_code,  # 短信校验接口返回数据
            "mobile": self.mobile,
            "userName": self.mobile,  # 不能重复
            "password": "test@123",
            "registerOrBind": 1,
            "validateType": 1
        }
        res = requests.put(url=self.user_register_url, json=data)
        print("登录后信息为：", res.text)


if __name__ == '__main__':
    cl = MemberRegister()
    # cl.send_msg()
    # cl.check_msg_code()
    cl.user_register()
