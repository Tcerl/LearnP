class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += '*' * self.width + '\n'
        return picture
    
    def get_amount_inside(self, shape):
        if not isinstance(shape, Rectangle):
            return 0
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.set_side(width)
    
    def set_height(self, height):
        self.set_side(height)
    
    def __str__(self):
        return f"Square(side={self.width})"



rect = Rectangle(10, 5)
print(rect.get_area())  # Output: 50
rect.set_height(3)
print(rect.get_perimeter())  # Output: 26
print(rect)  # Output: Rectangle(width=10, height=3)
print(rect.get_picture())
'''
Output:
'''

sq = Square(5)
print(sq.get_area())  # Output: 81
sq.set_side(4)
print(sq.get_diagonal())  # Output: 5.656854249492381
print(sq)  # Output: Square(side=4)
print(sq.get_picture())
'''
Output:
'''

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Output: 8
