class MathematicalOperation:
    #constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def addtion(self):
        return self.x + self.y
    #def subtration(self):
        #return self.num_x-self.num_y
    #def multiplication(self):
       # return self.num_x*self.num_y
   # def division(self):
        #return self.num_x/self.num_y
obj=MathematicalOperation(20,6)
print(f"{obj.x} + {obj.y} = {obj.addition()}")
    
        