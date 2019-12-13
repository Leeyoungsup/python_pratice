import time
class RacingCar :
    carName = ''
    def  __init__(self, name) :
        self.carName = name
    def runCar(self) :
        for _ in range(0, 3) :
            carStr = self.carName + '~~ 달립니다.\n'
            print(carStr, end = '')
            time.sleep(0.1)
car1 = RacingCar('@자동차1')
car2 = RacingCar('#자동차2')
car3 = RacingCar('$자동차3')
car1.runCar()
car2.runCar()
car3.runCar()
