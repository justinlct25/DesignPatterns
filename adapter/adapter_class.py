# also called wrapper
# wraps or adapts an existing implementation of a specific interface into another interface
import itertools

class InvalidPolygonError(Exception):
    pass


class Polygon(object):
    '''A polygon class'''

    def __init__(self, *sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def is_valid(self):
        # Do some complex stuff - not implemented in base class
        raise NotImplementedError
    
    def is_regular(self):
        # True if all sides are equal
        side = self.sides[0]
        return all([x==side for x in self.sides[1:]])

    def area(self):
        # Not implemented in base class
        raise NotImplementedError

class TriangleCA(Polygon):
    '''Triangle class from Polygon using class adapter'''
    
    def is_valid(self):
        '''Is the triangle valid'''
        perimeter = self.perimeter()
        for side in self.sides:
            sum_two = perimeter - side
            if sum_two <= side:
                raise InvalidPolygonError(str(self.__class__) + "is invalid!")
        return True

    def is_equilateral(self):
        if self.is_valid():
            return super(TriangleCA, self).is_regular()

    def is_isosceles(self):
        if self.is_valid():
            for a,b in itertools.combinations(self.sides, 2):
                if a == b:
                    return True
        return False

    def area(self):
        # Using Haron's formula
        p = self.perimeter()/2.0
        total = p
        for side in self.sides:
            total *= abs(p-side)
        
        return pow(total, 0.5)


class RectangleCA(Polygon):
    '''Rectangle class from Polygon using class adapter'''

    def is_square(self):
        if self.is_valid():
            return self.is_regular()

    def is_valid(self):
        '''Is the rectangle valid'''
        if len(self.sides) != 4:
            return False
        for a,b in [(0,2),(1,3)]:
            if self.sides[a] != self.sides[b]:
                return False
        return True

    def area(self):

        if self.is_valid():
            return self.sides[0]*self.sides[1]