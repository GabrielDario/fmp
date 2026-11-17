class Produto:
    def __init__(self, codigo, nome, categoria, preco, estoque, quantidade_vendida):
        self.codigo = int(codigo)
        self.nome = str(nome)
        self.categoria = str(categoria)
        self.preco = float(preco)
        self.estoque = int(estoque)
        self.quantidade_vendida = int(quantidade_vendida)

    def __str__(self):
        return (f"Cód: {self.codigo:04d} | {self.nome:<22} | Cat: {self.categoria:<12} | "
                f"R$ {self.preco:7.2f} | Est: {self.estoque:3d} | Vendidos: {self.quantidade_vendida:4d}")