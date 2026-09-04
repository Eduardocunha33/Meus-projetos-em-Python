class ArrayList:
    def __init__(self):
        self.LEN = 5
        self.arrayList = [None] * self.LEN
        self.insertPosition = 0

    def insert(self, data):
        if (self.isMemoryFull()):
            self.increaseMemory()
        self.arrayList[self.insertPosition] = data
        self.insertPosition += 1

    def remove(self):
        if (self.isEmpty()):
            print("Error")
            return
        self.insertPosition -= 1
        return self.arrayList[self.insertPosition]

    def isEmpty(self):
        return self.insertPosition == 0
            
        

    def isMemoryFull(self):
        return self.insertPosition == len(self.arrayList)

    
    def increaseMemory(self):
        newArray = [None] * (2 * len(self.arrayList) )
        self.copyElements(newArray, self.arrayList)
        self.arrayList = newArray
        newArray = None

    def copyElements(self, newArray, oldArray):
        for position in range(len(oldArray)):
            newArray[position] = oldArray[position]

    def print(self):
        for position in range(self.insertPosition):
            print(self.arrayList[position])

array = ArrayList()
array.insert("Ana")
array.insert("Beto")
array.insert("Carlos")
array.insert("Layla")
array.insert("Pedro")
array.remove()
array.print()