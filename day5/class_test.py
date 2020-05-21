class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print(self.__name, self.__score)
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self, name):
        self.__name = name
    def set_score(self, score):
        self.__score = score


std1 = Student('liwei', 90)
#std1.name='heheh'#可以在类外部修改private属性，但是建议用class set函数，因为可以对传人变量做判断
std1.age = 20#可以动态添加属性
print(std1.name)
print(std1.age)
std1.set_score(99)
print(std1.get_score())
#std1.print_score()
#std2 = Student('wangjie', 80)
#std2.print_score()


