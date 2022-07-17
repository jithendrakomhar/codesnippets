from unicodedata import name


class test_class:
    def __init__(self,id,name) -> None:
        self.id=id
        self.name=name

    def printname(self):
        print(self.name)


if __name__=="__main__":
    tc = test_class("10",'Rajesh')
    tc.printname()