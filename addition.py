class MathematicalOperation:
    #constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def addition(self):
        return self.x + self.y
    def subtration(self):
        return self.x-self.y
    def multiplication(self):
        return self.x*self.y
    def division(self):
        return self.x/self.y
obj=MathematicalOperation(20,6)
print(f"{obj.x}+{obj.y}={obj.addition()}")
print(f"{obj.x}-{obj.y}={obj.subtration()}")
print(f"{obj.x}*{obj.y}={obj.multiplication()}")
print(f"{obj.x}/{obj.y}={obj.division()}")
