from math import floor
class Rectangle():
    
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for h in range(self.height):
            for w in range(self.width):
                picture+="*"
            picture+="\n"
        print(picture)
        return picture

    def get_amount_inside(self,shape_2):
        if self.height / shape_2.height >= 0:
            h = floor(self.height / shape_2.height)
            if self.width /shape_2.width >= 0:
                w = floor(self.width/shape_2.width)
                return h*w
            else:
                return 0
        else:
            return 0
    
    
class Square(Rectangle):
    
    def  __init__(self,side):
        self.width = side
        self.height = side
    def __str__(self) -> str:
        return f"Square(side={self.width})"
    def set_side(self,side):
        self.width = side
        self.height = side
     
        
