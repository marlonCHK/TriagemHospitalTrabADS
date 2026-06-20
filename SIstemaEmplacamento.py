class NodoEstado:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla.upper()
        self.nomeEstado = nome_estado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tamanho = 10
        self.vetor = [None] *self.tamanho

    def funcaoHash(self, sigla):
        sigla = sigla.upper()

        #Exceção do DF que deve retornar 7
        if sigla == "DF":
            return 7
        
        charAscii1 = ord(sigla[0])
        charAscii2 = ord(sigla[1])
        posicao = (charAscii1 + charAscii2) % 10
        
        return posicao
    
    def Inserir(self, sigla, nome_estado):
        indice = self.funcaoHash(sigla)
        novoNodo = NodoEstado(sigla, nome_estado)

        novoNodo.proximo = self.vetor[indice]
        self.vetor[indice] = novoNodo

    def imprimirTabela(self):
        for i in range(self.tamanho):
            print(f"Posição [{i}]: ", end="")
            atual = self.vetor[i]

            if atual is None:
                print("Vazia")
            else:
                siglasPosicao = []

                while atual is not None:
                    siglasPosicao.append(atual.sigla)
                    atual = atual.proximo

                print(" -> ".join(siglasPosicao) + " -> None")