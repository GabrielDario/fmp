class Simbolo:
    def __init__(self, caractere, posicao):
        self.caractere = caractere
        self.posicao = posicao
        self.proximo = None


class ValidadorExpressoes:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def push(self, caractere, posicao):
        novo = Simbolo(caractere, posicao)
        novo.proximo = self.topo
        self.topo = novo

    def pop(self):
        if self.esta_vazia():
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        return removido

    def validar(self, expressao):
        self.topo = None  # Reseta a pilha
        pares = {')': '(', ']': '[', '}': '{'}
        aberturas = "([{"
        fechamentos = ")]}"

        for i, char in enumerate(expressao):
            if char in aberturas:
                self.push(char, i)
            elif char in fechamentos:
                if self.esta_vazia():
                    print(f"[Inválido] Fechamento '{char}' sem abertura na posição {i}.")
                    return False
                
                topo_elem = self.pop()
                if topo_elem.caractere != pares[char]:
                    print(f"[Inválido] Esperado par para '{topo_elem.caractere}' (pos {topo_elem.posicao}), mas encontrou '{char}' na posição {i}.")
                    return False

        if not self.esta_vazia():
            print(f"[Inválido] Sobrou delimitador aberto sem fechamento: '{self.topo.caractere}' na posição {self.topo.posicao}.")
            return False

        print(f"[Válido] Expressão correta: '{expressao}'")
        return True


# Testes Exercício 2
if __name__ == "__main__":
    print("\n=== TESTES: VALIDADOR DE EXPRESSÕES ===")
    validador = ValidadorExpressoes()

    validador.validar("(a+b) * [c-d]")
    validador.validar("{[(a+b)*c]}")
    validador.validar("([)]")
    validador.validar("((a+b)")
    validador.validar(")a+b(")