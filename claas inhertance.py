class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("Polygon is two dimensional shape")

    def cal_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def display_info(self):
        print("Triangle is a polygon with 3 sides")


class Quadrilateral(Polygon):
    def display_info(self):
        print("Quadrilateral is also Polygon with 4 sides")

t1 = Triangle([3,5,8])
perimeter = t1.cal_perimeter()
print("Perimeter is : ", perimeter)
s=[1,2,3,4]
q1 = Quadrilateral(s)
perimeter = q1.cal_perimeter()
print("Perimeter is : ", perimeter)

