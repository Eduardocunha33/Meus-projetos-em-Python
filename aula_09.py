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

# --- TESTANDO O CÓDIGO ---

tree = BinaryTree()

# Inserindo os nós na ordem do exercício inicial
values = [8, 3, 1, 5, 2, 15, 11, 16]
for val in values:
    tree.insert(val)

print("Pré-ordem:")
tree.preOrder()

print("\nEm-ordem:")
tree.inOrder()

print("\nPós-ordem:")
tree.postOrder()
