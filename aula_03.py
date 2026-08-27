class CleanerBot:
    def __init__(self, name = "", energyLevel = 360, isOn = False, color = "blue", waterCapacity = 50, positionX = 0, positionY = 0, local = 0, area = 0):
        self.name = name
        self.energyLevel = energyLevel
        self.isOn = isOn
        self.color = color
        self.waterCapacity = waterCapacity
        self.positionX = positionX
        self.positionY = positionY
        self.local = local
        self.area = area
    def turnOn(self):
        self.inOn = True

    def turnOff(self):
            self.inOn = False

    def showInfo(self):
        print(self.name)
        print(self.energyLevel)
        print(self.isOn)
        print(self.positionX)
        print(self.positionY)

    def addX(self, valueX):
        self.positionX += valueX

    def addX(self, valueY):
        self.positionX += valueY

    def changeX(self, newX):
        self.positionX += newX

    def changeY(self, newY):
        self.positionX += newY

samsumg = CleanerBot("S28 Ultra", 99, True, "black", 75, 60)
xiaomi = CleanerBot("xiaome", 85, False, "white")
xiaomi.changeX(90)
xiaomi.addX(20)
xiaomi.turnOn()
xiaomi.showInfo()
samsumg.showInfo()
