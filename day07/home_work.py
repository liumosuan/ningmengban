"""
"""

"""
题目1：定义函数，并通过给函数传递不同的参数(要想清楚哪些做为参数哦！！)：

一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），

如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。

编写一程序，询问购买价，再显示出折扣（%10或20%）和最终价格。
"""


class Test1:
    def __discount1(self, price):
        return price * 0.9

    def __discount2(self, price):
        return price * 0.8

    def test_01(self):
        try:
            price = int(input("请输入购买价格："))
            if 50 <= price <= 100:
                print("该商品折扣为10%")
                print("最终价格为：", self.__discount1(price))
            elif price > 100:
                print("该商品折扣为20%")
                print("该商品没有折扣", self.__discount2(price))
            else:
                print("该商品没有折扣")
                print("最终价格为：", price)
        except Exception as e:
            print("价格输入有误！")

"""
题目2：对前面知识做一个简单总结，自己梳理一下，重点复盘不太熟悉的知识点。

提交总结文件（txt, 思维导图,图片都可以）

总结:
辨别可变类型、不可变类型与有序类型、无序类型
    可变类型不可变类型：
    所谓可变类型，意思就是可以对整个元素进行修改，操作包括增删改
    注意：操作的是元素本身，而不是将数据进行复制、克隆之后再修改
    可变类型有：字典、list、集合
    不可变类型有：元组、字符串
    
    有序类型和无序类型：
    能用索引获取的就是有序
    有序类型：list、字符串、元组
    无序类型：字典、集合
    
一、字符串       
    字符串是不可变、有序类型
    1、字符串切片的规则是顾头不顾尾
    2、字符串切片的格式为str(start,end,step)  其中step默认为1
    3、a[::-1]倒序  a[0::2]取奇数位    a[1::2]取偶数位     a[:]为复制
    4、切片超出范围，不报错，和索引有区别。
    5、字符串的拼接用 "".join() 其中拼接连接符的选取可以在""中进行设置
    6、查找str.find(元素)  查找元素，找不到返回-1
       查找str.index(元素)  找不到则会报错
    7、替换 str.replace(old,new)
    8、分割  str.split(分隔符)
    

二、list
    list为可变、有序类型
    1、list里面嵌套list，嵌套的list只算一个元素长度
    2、倒序 a[::-1]    区间值 a[1:3]    步长为2 a[::2]        复制 a[::]
    3、增   list_test.append()  在列表最后追加
       list_test.insert(索引位置，要添加的值)  在指定位置添加元素、
    4、删   list_test.remove()  根据值进行删除
       list_test.pop(索引值)    根据索引进行删除
    5、改   list_test[2] = "demo"   根据索引位置进行值的修改
    6、升序list_test.sort()    降序 list_test.reverse()

三、dict
    dict为无序、可变类型
"""


"""
题目3：列表去重函数
定义一个函数 def remove_element(a_list):，
将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素(不能用集合去重，要使用for循环)
"""


class Test2:
    def test_01(self):
        a_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
        new_list = self.remove_element(a_list)
        print("去重后的a_list:", new_list)

    def remove_element(self, a_list):
        print("a_list:", a_list)
        new_list = []
        # for i in a_list:
        #     if i not in new_list:
        #         new_list.append(i)
        for i in a_list:
            # 如果i在new_list中就跳过，没有就添加到new_list中
            if i in new_list:
                continue
            else:
                new_list.append(i)
        return new_list


if __name__ == '__main__':
    # cl = Test1()
    # cl.test_01()

    cl = Test2()
    cl.test_01()
