from prod.model.entity import *
class Sorter:
    @staticmethod
    def sort(parking):
        if isinstance(parking, Parking):
            for i in range(len(parking) -1):
                for index in range(len(parking) -1 -i):
                    if parking[index].number > parking[index+1].number:
                        temp = parking[index]
                        parking[index] = parking[index + 1]
                        parking[index + 1] = temp


park = Parking(10)
print(park)

park.add(Transport(1,1, "BBBbbbbBBB"))
park.add(Transport(1,1, "Aaaaa"))
park.add(Transport(1,1, "Eeeeee"))
park.add(Transport(1,1, "Ddddd"))

print(park)

Sorter.sort(park)
