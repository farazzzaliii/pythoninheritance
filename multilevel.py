class Grandparent:
    def grandparent_method(self):
        print("This is a grandparent class method")

class Parent(Grandparent):
    def parent_method(self):
        print("This is a parent class method")

class Child(Parent):
    def child_method(self):
        print("This is a child class method")

child_obj = Child()


child_obj.grandparent_method()
child_obj.parent_method()
child_obj.child_method()