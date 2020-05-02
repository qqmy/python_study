'''
需求
1、房子有户型，总面积和家具名称列表
新房子没有任何的家具
2、家具有名字和占地面积，其中
席梦思占地4平米
衣柜占地2平米
餐桌占地1.5平米
3、将以上三件家具添加到房中
1、打印房子是，要求输出：户型，总面积，剩余面积，家具名称列表

剩余面积
1、在创建房子对象是，定义一个剩余面积的属性，初始值和总面积相等
1、当调用add_item方法的时候，想房间添加家具是，让剩余面积>=家具面积类

属性：house_type,house_area,item_list,free_area
方法：_init_, _str_,add_item
类：houseItem
属性：name，area
方法：_init_
'''
# 先写家具类
age = 10
print(f"{age}")

class House():
    def __init__(self,house_type,house_area):
        self.type = house_type
        self.area = house_area
        self.free = self.area
        self.item_list = []
    def __str__(self):
        return f"{self.type}总面积{self.area}剩余面积{self.free}"
    def add_item(self,item):

        if item.area<self.free:
            self.item_list.append(item.name)
            self.free = self.free-item.area
            print(f'家具：{self.item_list}')
        else:
            print('该换房子了')


class Furnishing():
    def __init__(self,name,area):
        self.name = name
        self.area = area


house = House('别墅',120)
guizi = Furnishing('柜子',10)
zhuozi = Furnishing('桌子',100)
house.add_item(guizi)
house.add_item(zhuozi)