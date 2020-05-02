'''
角色：学校，学员，课程，讲师，班级
要求：
1、创建北京，上海2所学校
2、创建linux，python，go 3个课程，linux、py在北京开，go在上海开
3、课程包含，周期，价格，通过学校创建课程
4、通过学校创建班级，班级关联课程，讲师
5、创建学员时，选择学校，关联班级
6、创建讲师角色时要关联学校
7、提供三个角色接口，讲师，学生，管理员
8、学员视图，可以注册，交学费，选择班级
9、讲师视图，讲师可管理自己的班级，上课时选择班级，查看班级学员列表，修改所管理的学员成绩
10、管理视图，创建讲师，创建班级，创建课程
11、上面的操作产生的数据都通过pickle序列化保存到文件里
'''
# 学校
class School():
    def __init__(self,school_address):
        self.school_address = school_address
        self.course_list = []
        self.class_list = []

    def create_course(self,course):
        print(self.school_address,'开设了课程：',course.course_name)
        self.course_list.append(course)

    def show_course(self):
        course = [i.course_name for i in self.course_list]
        return course

    def create_class(self,course,teacher):
        if course in self.course_list:
            class_name = Classes(course.course_name,course,teacher)
            self.course_list.append(class_name)
        else:
            print('班级创建失败，该学校没有该课程')


# 讲师
class Teacher():
    def __init__(self,teacher_name,salary):
        self.teacher_name = teacher_name
        self.salary = salary

    def choose_school(self,school):
        pass

# 课程
class Course():
    def __init__(self,course_name,period,price):
        self.course_name = course_name
        self.period = period
        self.price = price
# 学员
class Student():
    def __init__(self,stu_name):
        self.stu_name = stu_name
        self.school = None
        self.class_name = None

    def choose_school(self,school):
        self.school = school

    def choose_class(self,class_name):
        class_obj = None
        if not self.school:
            print('选择班级失败，请先选择学校')
            return

        class_list = self.school.class_list
        for classs in class_list:
            if classs.class_name == class_name:
                class_obj = classs
                break

        if class_obj:
            print('选择班级成功')
            self.class_name = class_obj
        else:
            print('选择学校失败，该学校没有这个班级')

        # if self.school :
        #     # self.class_name = class_name
        #     class_list = self.school.class_list
        #     for classs in class_list:
        #         if classs.class_name == class_name:
        #             class_obj = classs
        #             break
        #     if class_obj:
        #         print('选择班级成功')
        #         self.class_name = class_obj
        #     else:
        #         print('选择学校失败，该学校没有这个班级')
        # else:


class Classes():
    def __init__(self,class_name,course,teacher):
        self.class_name = class_name
        self.course = course
        self.teacher = teacher

if __name__ == '__main__':
    # 创建学校
    school_beijing = School('北京')
    school_shagnhai = School('上海')

    # 给学校创建课程
    course_linux = Course('linux','20周',1000)
    course_python = Course('python','30周',3000)
    course_go = Course('go','18周',900)
    school_beijing.create_course(course_linux)
    school_beijing.create_course(course_python)
    school_shagnhai.create_course(course_go)
    print(school_beijing.show_course())

    # 给学校创建班级
    school_beijing.create_class(course_linux,'choubaoguai')
    school_beijing.create_class(course_python,'choub')
    school_shagnhai.create_class(course_go,'lyx')

    # 创建学员
    s1 = Student('s1')
    s1.choose_school(school_beijing)
    s1.choose_class('linux')


