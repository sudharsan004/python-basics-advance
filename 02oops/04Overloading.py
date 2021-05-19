class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.coordinates =(x,y)
    
    # Dunder methods
    # the functions between the objs can be defined in the class via add sub mul etc methods ..
    def __add__(self, p):
        return Point(self.x+p.x,self.y+p.y)

    def __mul__(self, p):
        return Point(self.x*p.x,self.y*p.y)

    def __str__(self):
        return f'coordinates are: {str(self.coordinates)}'


p1=Point(5,3)
p2=p1+p1
print(p2)
p3=p2*p1
print(p3)

    