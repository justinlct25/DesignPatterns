import itertools
from adapter_class import InvalidPolygonError, Polygon

class TriangleOA(object):
    '''Triangle class from Polygon using object adapter'''

    def __init__(self, *sides):
        self.polygon = Polygon(*sides)

    def perimeter(self):
        return self.polygon.perimeter()

    def is_valid(f):
        def inner(self, *args):
            # Sum of 2 sides should be > 3rd side
            perimeter = self.polygon.perimeter()
            sides = self.polygon.sides

            for side in sides:
                sum_two = perimeter - side
                if sum_two <= side:
                    raise InvalidPolygonError(str(self.__class__) + "is invalid!")
            result = f(self, *args)
            return result
        return inner

    @is_valid
    def is_equilateral(self):
        return self.polygon.is_regular()

    @is_valid
    def is_isosceles(self):
        for a,b in itertools.combinations(self.polygon.sides, 2):
            if a == b:
                return True
        return False

    def area(self):
        p = self.polygon.perimeter()/2.0
        total = p

        for side in self.polygon.sides:
            total *= abs(p-side)
        
        return pow(total, 0.5)


class RectangleOA(object):
    '''Rectangle class from Polygon using object adapter'''

    method_mapper = {'is_square': 'is_regular'}

    def __init__(self, *sides):
        self.polygon = Polygon(*sides)

    def is_valid(f):
        def inner(self, *args):
            sides = self.sides
            if len(sides) !=4:
                return False

            for a,b in [(0,2),(1,3)]:
                if sides[a] != sides[b]:
                    return False

            result = f(self, *args)
            return result
        return inner

    def __getattr__(self, name):
        ''' Overloaded __getattr__ to forward methods to wrapped instance'''
        if name in self.method_mapper:
            w_name = self.method_mapper[name]
            return getattr(self.polygon, w_name)
        else:
            return getattr(self.polygon, name)

    @is_valid # decorator
    def area(self):
        '''Return area of rectangle'''
        sides = self.sides
        return sides[0]*sides[1]