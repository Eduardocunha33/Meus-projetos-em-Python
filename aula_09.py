class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # cria o nó que vai ser inserido na árvore
        newNode = Node(data)

        # verifica se a árvore está vazia, se estiver, o nó inserido será a raiz da árvore
        if (self.isEmpty()):
            self.root = newNode
            return

        self.insertRecursive(self.root, newNode)

    def insertRecursive(self, currentNode, newNode):
        # verifica se o nó da esquerda é None, se for, insere o novo nó na esquerda
        if newNode.value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = newNode
            else:
                self.insertRecursive(currentNode.left, newNode)
        else:
            if currentNode.right is None:
                currentNode.right = newNode
            else:
                self.insertRecursive(currentNode.right, newNode)

    # retorna True se a árvore estiver vazia, caso contrário, retorna False
    def isEmpty(self):
        return self.root == None


    # 1. Pré-ordem (Raiz, Esquerda, Direita)
    def preOrder(self):
        self.preOrderRecursive(self.root)
        print() 

    def preOrderRecursive(self, node):
        if node is not None:
            print(node.value, end=" ")       
            self.preOrderRecursive(node.left)  
            self.preOrderRecursive(node.right) 

    # 2. Em-ordem (Esquerda, Raiz, Direita)
    def inOrder(self):
        self.inOrderRecursive(self.root)
        print()

    def inOrderRecursive(self, node):
        if node is not None:
            self.inOrderRecursive(node.left)   
            print(node.value, end=" ")       
            self.inOrderRecursive(node.right)  

    # 3. Pós-ordem (Esquerda, Direita, Raiz)
    def postOrder(self):
        self.postOrderRecursive(self.root)
        print()

    def postOrderRecursive(self, node):
        if node is not None:
            self.postOrderRecursive(node.left)   
            self.postOrderRecursive(node.right)  
            print(node.value, end=" ")         


tree = BinaryTree()

# Inserindo os nós na ordem do exercício inicial
values = [8, 3, 1, 5, 2, 15, 11, 16]
for val in values:
    tree.insert(val)

print("Pre-order:")
tree.preOrder()

print("\nIn-order:")
tree.inOrder()

print("\nPost-order:")
tree.postOrder()

"""
class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        #cria o no que vai ser inserido na arvore
        newNode = Node(data)
        
        #Verifica se arvore esta vazia e caso sim insere na raiz
        if (self.isEmpty()):
            self.root = newNode
            return
        
        #insere recurvivamente na arvore
        self.insertRecursive(self.root, newNode)
    
    def insertRecursive(self, currentNode, newNode):
        #verifica se o novo no sera inserido na esquerda
        if newNode.data < currentNode.data:
            #Filho do no visitado é nulo (vai ser inserido nesta posicao)
            if currentNode.left is None:
                currentNode.left = newNode
            #chama a funcao recursivamente para a esquerda
            else:
                self.insertRecursive(current.left, newNode)
        
        #Verifica se o novo no sera inserido a direita
        else:
            if currentNode.right is None:
                currentNode.right = newNode
             #chama a funcao recursivamente para a direita
            else:
                self.insertRecursive(current.right, newNode)
            
    
    #retorna verdadeiro se arvore vazia (root = none) ou arvore com pelo menos
    #1 elemento (retorna isEmpty = false)
    def isEmpty(self):
        return self.root == None
        

tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(15)

print(tree.root.data)
print(tree.root.left.data)
print(tree.root.right.data)












class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def insert(self, data):
        #testa se a lista esta vazia e insere o primeiro 
        newNode = Node(data)
        self.size += 1
        if (self.isEmpty()):
            self.first  = self.last = newNode
            return
        self.last.next = self.last = newNode
    
    def removeAt|(self, position):
        pass
        
    def insertAt(self, position, data):
        pass
    
    def remove(self):
        #remocao com lista vazia
        if (self.isEmpty()):
            print("Erro nao tem o que remover meu filho")
            return
        #remocao com somente 1 elemento na lista
        if (self.size == 1):
            #primeiro e o ultimo vao apontar para nada
            copy = self.last
            self.last = self.first = None
            self.size -= 1
            return copy
            
        #remocao de lista com varios elementos
        copy = self.last
        temp = self.first
        for _ in range(0, self.size - 2):
            temp = temp.next
        self.size -= 1    
        last = temp
        last.next = None
        return copy
        
    def printList(self):
        temp = self.first
        while(temp != None):
            print(temp.data)
            temp = temp.next
        
    def isEmpty(self):
        return self.first == None
    
    
list = LinkedList()
list.insert("Beto")
list.insert("Ana")
list.insert("Bia")

list.printList()


"""