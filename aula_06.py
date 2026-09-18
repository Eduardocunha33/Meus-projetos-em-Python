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

    # ==========================================
    # BLOCO 3: Método de Inserção
    # ==========================================
    def insert(self, data):

        newNode = Node(data)  # Cria um novo Nó com o dado que queremos inserir.

        if (self.isEmpty()):             # Checa se a lista está vazia.
            self.first = newNode      # Se sim, o primeiro elemento da lista passa a ser este novo Nó.
            return

        # se a lista não estiver vazia, precisamos percorrer a lista até o último elemento e insere no final.
        temp = self.first
        while (temp.next != None):      # Enquanto houver um próximo elemento...
            temp = temp.next             # ...passa para o próximo elemento.
        temp.next = Node(data)          # Adiciona o novo nó no final da lista.

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
list.printList()  # Imprime todos os elementos da lista.