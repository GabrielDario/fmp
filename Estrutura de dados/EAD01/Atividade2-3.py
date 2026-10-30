class Caixa:
    def __init__(self, codigo, produto, peso):
        self.codigo = codigo
        self.produto = produto
        self.peso = peso
        self.proximo = None


class ControleCaixas:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def _existe_codigo(self, codigo):
        atual = self.topo
        while atual:
            if atual.codigo == codigo:
                return True
            atual = atual.proximo
        return False

    # 1. Empilhar uma caixa (com prevenção de código duplicado)
    def push(self, codigo, produto, peso):
        if self._existe_codigo(codigo):
            print(f"Erro: Já existe uma caixa com o código '{codigo}'.")
            return False
        novo = Caixa(codigo, produto, peso)
        novo.proximo = self.topo
        self.topo = novo
        print(f"Caixa '{codigo}' ({produto}) empilhada com sucesso.")
        return True

    # 2. Consultar a caixa do topo
    def peek(self):
        if self.esta_vazia():
            return None
        return self.topo

    # 3. Retirar a caixa do topo
    def pop(self):
        if self.esta_vazia():
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        removido.proximo = None
        return removido

    # 4. Exibir da caixa superior até a base
    def listar(self):
        if self.esta_vazia():
            print("Pilha de caixas vazia.")
            return
        print("\n--- Pilha de Caixas (Topo à Base) ---")
        atual = self.topo
        while atual:
            print(f"Código: {atual.codigo} | Produto: {atual.produto} | Peso: {atual.peso}kg")
            atual = atual.proximo
        print("-" * 40)

    # 5. Calcular o peso total
    def calcular_peso_total(self):
        total = 0
        atual = self.topo
        while atual:
            total += atual.peso
            atual = atual.proximo
        return total

    # 7. Retirar caixas até localizar um código informado, usando uma pilha auxiliar
    def retirar_ate_codigo(self, codigo_alvo):
        if self.esta_vazia():
            print("Pilha vazia.")
            return False

        if not self._existe_codigo(codigo_alvo):
            print(f"Código '{codigo_alvo}' não encontrado no depósito.")
            return False

        pilha_aux = [] # Usando lista simples como pilha auxiliar

        # Transfere para a auxiliar até achar o alvo
        while self.topo and self.topo.codigo != codigo_alvo:
            removido = self.pop()
            pilha_aux.append(removido)

        # Remove o alvo localizado no topo atual
        alvo = self.pop()
        print(f"-> Caixa alvo '{alvo.codigo}' ({alvo.produto}) retirada com sucesso.")

        # Restaura os elementos da auxiliar de volta para a pilha principal
        while pilha_aux:
            reg = pilha_aux.pop()
            reg.proximo = self.topo
            self.topo = reg

        return True


# Testes Exercício 3
if __name__ == "__main__":
    print("\n=== TESTES: CONTROLE DE CAIXAS EM DEPÓSITO ===")
    deposito = ControleCaixas()

    # Pilha vazia
    deposito.listar()

    # Empilhando caixas
    deposito.push("C01", "Parafusos", 12.5)
    deposito.push("C02", "Arruelas", 8.0)
    deposito.push("C03", "Brocas", 5.0)
    deposito.push("C04", "Martelos", 20.0)

    deposito.listar()
    print(f"Peso total no depósito: {deposito.calcular_peso_total()}kg")

    # Tentativa de código duplicado
    deposito.push("C02", "Outro produto", 10.0)

    # Caixa procurada no topo (C04)
    print("\n[Teste] Retirando caixa no topo:")
    deposito.retirar_ate_codigo("C04")
    deposito.listar()

    # Caixa procurada na base (C01)
    print("\n[Teste] Retirando caixa na base:")
    deposito.retirar_ate_codigo("C01")
    deposito.listar()

    # Código inexistente
    print("\n[Teste] Buscando código inexistente:")
    deposito.retirar_ate_codigo("C99")