from builder import *

# without builder pattern
house = LegoHouse(nrooms=1, nporches=1)
print('----without builder pattern----')
print(house)

room = Room(nwindows=1)
house.add_room(room)
# house.add_room(room)
porch = Porch()
house.add_porch(porch)
print(house)


# with builder pattern
# sparing code / efforts
# ensure actual number of objects(rooms, porchs) consistence with the number (nrooms, nporchs)
builder1 = LegoHouseBuilder(nrooms=2, nporches=1, nwindows=1)
print('----with builder pattern-----')
print(builder1.build())

builder2 = LegoHouseBuilder(nrooms=2, nporches=1, nwindows=1)
print(builder2.build())

# encapsulate a kind of house in a subclass of the Builder
small_house = SmallLegoHouseBuilder().build()
print('----small house----')
print(small_house)

# build many of them
houses = list(map(lambda x: SmallLegoHouseBuilder().build(), range(100)))
print('----build many of them----')
print(houses[0])
print(houses[11])
print(len(houses))

# north facing houses
print('----build north-facing house----')
print(NorthFacingHouseBuilder(nrooms=2, nporches=1, nwindows=1))
print(NorthFacingSmallHouseBuilder().build())