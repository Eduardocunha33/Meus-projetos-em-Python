# ==========================================
# BLOCO 1: Classe Node (Nó)
# O Nó é a "peça" fundamental da lista encadeada. 
# Ele guarda a informação e aponta para a próxima peça.
# ==========================================
class Node:
    # O método __init__ é o construtor. Ele roda sempre que criamos um novo Node.
    def __init__(self, data):
        self.data = data    # Guarda o valor/dado que você quer armazenar (ex: um número ou texto)
        self.next = None    # Aponta para o próximo Nó da lista. Começa vazio (None).


# ==========================================
# BLOCO 2: Classe LinkedList (Lista Encadeada)
# Esta classe gerencia a lista inteira, controlando onde ela começa.
# ==========================================
class LinkedList:
    # Cria a lista inicialmente vazia.
    def __init__(self):
        self.first = None   # 'first' (ou cabeça/head) indica quem é o primeiro Nó da lista.
        self.last = None
        self.size = 0

    # ==========================================
    # BLOCO 3: Método de Inserção
    # ==========================================
    def insert(self, data):

        newNode = Node(data)  # Cria um novo Nó com o dado que queremos inserir.
        self.size += 1          # Incrementa o tamanho da lista.
        if (self.isEmpty()):             # Checa se a lista está vazia.
            self.first = self.last = newNode      # Se sim, o primeiro elemento da lista passa a ser este novo Nó.
            return

        self.last.next = self.last = newNode  # Se não, o último elemento da lista aponta para este novo Nó e o último elemento passa a ser este novo Nó.

    def remove(self):
        if (self.isEmpty()):
            print("Lista vazia. Não há elementos para remover.")
            return

        if (self.size == 1):
            copy = self.last 
            self.last = self.first = None
            self.size -= 1
            return copy.data 


        
        while self.first.next != self.last:
            self.first = self.first.next

            
                

    #imprime lista
    def printList(self):
        temp = self.first
        while (temp != None):           # Enquanto houver um próximo elemento...
            print(temp.data)             # ...imprime o dado do elemento atual.
            temp = temp.next             # Passa para o próximo elemento.

    # ==========================================
    # BLOCO 4: Método de Verificação (Vazia)
    # ==========================================
    def isEmpty(self):
        # Retorna True (Verdadeiro) se o 'first' for None (ou seja, se a lista estiver vazia).
        return self.first == None


# ==========================================
# BLOCO 5: Execução do Código
# ==========================================
list = LinkedList()       # Cria uma nova lista encadeada (ela nasce vazia, first = None).

# Tenta imprimir o dado do primeiro elemento da lista.

list = LinkedList()       # Cria uma nova lista encadeada (ela nasce vazia, first = None).
list.insert("Ana")       # Adiciona o primeiro elemento da lista.
list.insert("Beto")      # Adiciona o segundo elemento da lista.
list.insert("Carlos")    # Adiciona o terceiro elemento da lista.
list.insert("Layla")     # Adiciona o quarto elemento da lista.
list.remove()  # Remove o primeiro elemento da lista.
list.remove()  # Remove o segundo elemento da lista.
list.remove()


list.printList()  # Imprime todos os elementos da lista.