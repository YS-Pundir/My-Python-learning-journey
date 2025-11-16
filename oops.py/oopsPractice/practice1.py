# calculaeting the area and parimeter of the circle
class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    @property
    def Area(self):
        return 3.14*self.radius**2
    
    
    def parimeter(self):
        return 2*3.14*self.radius
    
    
    def volume(self):
        return 3.14*self.radius**3
    
circle1=Circle(4)
print("the area of the circcle is ",circle1.Area())
print("the  perimeter of the circle is ",circle1.parimeter())
print("the volume of the circle is ",circle1.volume())
    