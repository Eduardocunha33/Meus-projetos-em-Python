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

    def  removeAt(self, position):
        if (self.isEmpty()):
            print("Error")
            return
        
        if (position < 0 or position >= self.insertPosition):
            print("Error")
            return
        
        data = self.arrayList[position]
        for i in range(position, self.insertPosition - 1):
            self.arrayList[i] = self.arrayList[i + 1]

        self.insertPosition -= 1
        self.arrayList[self.insertPosition] = None
        return data

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
"""
array = ArrayList()
array.insert("Ana")
array.insert("Beto")
array.insert("Carlos")
array.insert("Layla")
array.insert("Pedro")
array.remove()
array.print()
"""
#usando o conceito de herança para aproveitar tudo que ja foi desenvolvido na lista
class Stack(ArrayList):
    #função da pilha que insere
    def push(self, data):
        self.insert(data)

    #função da pilha que remove
    def pop(self):
        return self.remove()

#Usando o conceito de herança para aproveitar tudo que ja foi desenvolvido na lista
class Queue(ArrayList):

    #função da fila que insere
    def enqueue(self, data):
        self.insert(data)

    #função da fila que remove
    def dequeue(self):
        return self.removeAt(0)
    
#instanciando um objeto fila e usando seus métodos
queue = Queue()
queue.enqueue("Ana")
queue.enqueue("Beto")   
queue.enqueue("Carlos")
queue.enqueue("João")

"""
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
"""
#instanciando um objeto pilha e usando seus métodos
stack = Stack()
stack.push("Ana")
stack.push("Beto")
stack.push("Carlos")
stack.push("João")

#removendo os elementos da pilha e imprimindo-os
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())