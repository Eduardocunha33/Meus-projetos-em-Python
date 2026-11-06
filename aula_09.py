class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

no = Node(34)

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #cria o nó que vai ser inserido na árvore
        newNode = Node(data)

        #verifica se a árvore está vazia, se estiver, o nó inserido será a raiz da árvore
        if (self.isEmpty()):
            self.root = newNode
            return

        self.insertRecursive(self.root, newNode)

    def insertRecursive(self, currentNode, newNode):
        #verifica se o nó da esquerda é None, se for, insere o novo nó na esquerda, caso contrário, chama a função recursivamente para o nó da esquerda
        if newNode.value < currentNode.value:
            #filho do nó visitado é None, insere o novo nó na esquerda
            if currentNode.left is None:
                currentNode.left = newNode

            else:
                self.insertRecursive(currentNode.left, newNode)
        
        else:
            if currentNode.right is None:
                currentNode.right = newNode
            else:
                self.insertRecursive(currentNode.right, newNode)

    #retorna True se a árvore estiver vazia, caso contrário, retorna False
    def isEmpty(self):
        return self.root == None

tree = BinaryTree()

tree.insert(8)
tree.insert(3)
tree.insert(15)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
