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
            print(f"|{atual.cor} {atual.numero}| ", end="")
            atual = atual.proximo

    def atenderPaciente(self):
        atual = self.head
        anterior = None

        self.head = atual.proximo
        return True


lista = ListaEncadeada()

while True:
    print("-"*10)
    print("Menu")
    print("-"*10)
    print(" 1 - Adicionar paciente a fila\n 2 - Mostrar pacientes na fila\n 3 - Chamar paciente\n 4 - Sair")
    escolha = input()

    if escolha == "1":
        lista.inserir()

    elif escolha == "2":
        lista.imprimirListaEspera()

    elif escolha == "3":
        lista.atenderPaciente()

    else:
        break

        
