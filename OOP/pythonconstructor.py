class TestClass():
    def __init__(self):
        print("I am Printing from constructor") #Constructor will be printed always whatever other fuction does

    def fun1(self):
        print("I am Fuction one")

    def fun2(self):
        print("I am another fuction")

MyObject = TestClass()

MyObject.fun1()  # Here i called fun1 but it will be print both fun1 and constructor

