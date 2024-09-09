class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

#  print("in init")

    def config(self):
        print("config is",self.cpu,self.ram)


comp1 = Computer('i5', 16)
comp2 = Computer('i6', 20)

comp1.config()
comp2.config()