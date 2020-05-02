# 数值定制
class Time60():
    def __init__(self,hr,min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return f"{self.hr} : {self.min}"

    # _repr_ = __str__()

    def __add__(self, other):

        # 调用self.__class__相当于调用Time60（）
        return self.__class__(self.hr+other.hr,self.min+other.min)

    def __iadd__(self, other):
        self.hr +=other.hr
        self.min +=other.min
        return self
t1 = Time60(10,39)
t2 = Time60(1,20)
print(t1+t2)
t1 += t2
print(t1)

