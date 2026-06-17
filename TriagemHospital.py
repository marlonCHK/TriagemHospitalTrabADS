class Nodo:
    contador = 1
    contador_A = 201
    def __init__(self, cor):
        if(cor == "A"):
            self.numero = Nodo.contador_A
            Nodo.contador_A += 1
        else:
            self.numero = Nodo.contador
            Nodo.contador += 1
            
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self):
        print("Qual cor será solicitada ? (A) , (V)")
        cor = input()

        if cor == "A":
            self.inserirComPrioridade(cor)
        elif cor == "V":
            self.inserirSemPrioridade(cor)
    
    def inserirComPrioridade(self, cor):
        novo_nodo = Nodo(cor)
        atual = self.head
        anterior = None

        #percorre ate estar ordenado
        while atual is not None and atual.numero < novo_nodo.numero and atual.numero > 200:
            anterior = atual
            atual = anterior.proximo

        if anterior is None:
            novo_nodo.proximo = self.head
            self.head = novo_nodo

        else:
            anterior.proximo = novo_nodo
            novo_nodo.proximo = atual

    def inserirSemPrioridade(self, cor):
        novo_nodo = Nodo(cor)

        #lista vazia
        if self.head is None:
            self.head = novo_nodo
            return
        
        #percorre para adicionar no final
        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo
        
        atual.proximo = novo_nodo
    
    def imprimirListaEspera(self):
        atual = self.head
        while atual is not None:
            print(f"|{atual.cor} {atual.numero}| => ", end="")
            atual = atual.proximo


lista = ListaEncadeada()
for i in range(5):
    lista.inserir()

lista.imprimirListaEspera()