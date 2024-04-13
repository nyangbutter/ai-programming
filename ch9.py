#2-6
class Car:
    def method(self):
        print('슈퍼클래스')
class Sedan(Car):
    def method(self):
        print('서브 클래스')
myCar=Car()
mySedan=Sedan()
myCar.method()
mySedan.method()

#6-7
class Car:
    speed=0
    def upSpeed(self,value):
        self.speed+=value
class RVCar(Car):
    seatNum=0
    def getSeatNum(self):
        return self.SeatNum
