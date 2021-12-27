# builder pattern separates out the construction of an object from its representation
# same construction process can be used to build different representation
# in other words, using it can conveniently create different types or representative instances of the same class
#   (build slightly different variation on the same class)
class Room(object):

    def __init__(self, nwindows=2, doors=1, direction='S'):
        self.nwindows = nwindows
        self.doors = doors
        self.direction = direction

    def __str__(self):
        return "Room <facing:%s, windows=#%d> " % (self.direction, self.nwindows)

class Porch(object):

    def __init__(self, ndoors=2, direction='W'):
        self.ndoors = ndoors
        self.direction = direction

    def __str__(self):
        return "Porch <facing:%s, doors=#%d> " % (self.direction, self.ndoors)

class LegoHouse(object):

    def __init__(self, nrooms=0, nporches=0, nwindows=0):
        self.nporches = nporches
        self.nrooms = nrooms
        self.rooms = []
        self.porches = []
        self.nwindows = nwindows

    def __str__(self):
        msg="LegoHouse<rooms=#%d, porches=#%d>: " % (self.nrooms, self.nporches)

        for i in self.rooms:
            msg += str(i)

        for i in self.porches:
            msg += str(i)

        return msg

    def add_room(self, room):
        self.rooms.append(room)

    def add_porch(self, porch):
        self.porches.append(porch)



# builder pattern
class LegoHouseBuilder(object):

    def __init__(self, *args, **kwargs):
        self.house = LegoHouse(*args, **kwargs)

    def build(self):

        self.build_rooms()
        self.build_porches()
        return self.house

    def build_rooms(self):
        for i in range(self.house.nrooms):
            room = Room(self.house.nwindows)
            self.house.add_room(room)

    def build_porches(self):
        for i in range(self.house.nporches):
            porch = Porch(1)
            self.house.add_porch(porch)

# encapsulated kinds of house
class SmallLegoHouseBuilder(LegoHouseBuilder):

    def __init__(self):
        self.house = LegoHouse(nrooms=2, nporches=1, nwindows=2)

class NorthFacingHouseBuilder(LegoHouseBuilder):

    def build_rooms(self):
        for i in range(self.house.nrooms):
            room = Room(self.house.nwindows, direction='N')
            self.house.add_room(room)

    def build_porches(self):
        for i in range(self.house.nporches):
            porch = Porch(1, direction='N')
            self.house.add_porch(porch)

class NorthFacingSmallHouseBuilder(NorthFacingHouseBuilder, SmallLegoHouseBuilder):
    pass