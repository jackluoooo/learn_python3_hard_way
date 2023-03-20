# 继承和组合

# 隐藏式继承
# class Parent(object):
#     def implicit(self):
#         print("Parent implicit")
#
#
# class Child(Parent):
#     pass
#
#
# dad = Parent()
# son = Child()
# dad.implicit()
# son.implicit()

# 显示继承
# class Parent(object):
#     def override(self):
#         print("PARENT override()")
#
#
# class Child(Parent):
#     def override(self):
#         print("child override()")
#
#
# dad = Parent()
# son = Child()
# dad.override()
# son.override()

# 在运行前和运行后替换
class Parent(object):
    def altered(self):
        print("Parent altered")


class Child(Parent):
    def altered(self):
        print("CHILD ,BEFORE PARENT altered")
        super(Child, self).altered()
        print("CHILD,After Parent altered")


dad = Parent()
son = Child()

dad.altered()
son.altered()
