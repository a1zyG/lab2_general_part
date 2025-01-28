class Furniture:
    def __init__(self, kg, floor, k):
        self.kg = kg
        self.floor = floor
        self.k = k
    def result(self):
        cost = 0
        if (kg < 50):
            cost = 300
        elif (kg >= 50 and  kg < 100):
            cost = 1000
        else:
            cost = 2000
        return cost


kg, floor, k =  map(int,input().split()) # если k = 1, то груз можно поднять на лифте. Иначе - 0
Furnt = Furniture(kg, floor, k)
print(Furnt.result())