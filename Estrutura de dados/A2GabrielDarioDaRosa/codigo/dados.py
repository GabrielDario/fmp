
from models import Produto


def carregar_dados_iniciais():
    return [
      Produto(105, "Teclado Mecânico RGB", "Periféricos", 350.00, 15, 120),
        Produto(101, "Mouse Gamer Wireless", "Periféricos", 220.50, 30, 340),
        Produto(112, "Monitor 27' 144Hz", "Monitores", 1450.00, 8, 85),
        Produto(103, "Headset Surround 7.1", "Áudio", 299.90, 22, 210),
        Produto(108, "SSD NVMe 1TB", "Armazenamento", 480.00, 40, 500),
        Produto(102, "Webcam Full HD", "Vídeo", 189.00, 12, 95),
        Produto(110, "Cadeira Ergonômica", "Mobiliário", 1150.00, 5, 42),
        Produto(104, "Hub USB-C 7 em 1", "Acessórios", 145.00, 50, 410),
        Produto(119, "Placa de Vídeo RTX 4060", "Hardware", 2199.90, 6, 60),
        Produto(107, "Memória RAM 16GB DDR5", "Hardware", 380.00, 35, 290),
        Produto(115, "Processador Ryzen 7", "Hardware", 1650.00, 10, 115),
        Produto(106, "Fonte 650W 80 Plus", "Hardware", 410.00, 18, 175),
        Produto(120, "Gabinete Mid Tower", "Hardware", 320.00, 14, 130),
        Produto(109, "Mousepad Speed Extra G", "Acessórios", 89.90, 60, 620),
        Produto(114, "Microfone Condensador", "Áudio", 430.00, 9, 88),
        Produto(118, "Caixa de Som Bluetooth", "Áudio", 260.00, 25, 310),
        Produto(111, "Roteador Wi-Fi 6", "Redes", 390.00, 19, 145),
        Produto(117, "Cabo HDMI 2.1 2m", "Acessórios", 55.00, 80, 750),
        Produto(113, "Suporte Articulado", "Mobiliário", 175.00, 27, 230),
        Produto(116, "Notebook Ultrafino i5", "Computadores", 3490.00, 4, 38),
    ]
def carregar_dados_aleatorios():
    """Cenário 1: Ordem desordenada / aleatória (Caso Médio)"""
    return [
        Produto(105, "Teclado Mecânico RGB", "Periféricos", 350.00, 15, 120),
        Produto(101, "Mouse Gamer Wireless", "Periféricos", 220.50, 30, 340),
        Produto(112, "Monitor 27' 144Hz", "Monitores", 1450.00, 8, 85),
        Produto(103, "Headset Surround 7.1", "Áudio", 299.90, 22, 210),
        Produto(108, "SSD NVMe 1TB", "Armazenamento", 480.00, 40, 500),
        Produto(102, "Webcam Full HD", "Vídeo", 189.00, 12, 95),
        Produto(110, "Cadeira Ergonômica", "Mobiliário", 1150.00, 5, 42),
        Produto(104, "Hub USB-C 7 em 1", "Acessórios", 145.00, 50, 410),
        Produto(119, "Placa de Vídeo RTX 4060", "Hardware", 2199.90, 6, 60),
        Produto(107, "Memória RAM 16GB DDR5", "Hardware", 380.00, 35, 290),
        Produto(115, "Processador Ryzen 7", "Hardware", 1650.00, 10, 115),
        Produto(106, "Fonte 650W 80 Plus", "Hardware", 410.00, 18, 175),
        Produto(120, "Gabinete Mid Tower", "Hardware", 320.00, 14, 130),
        Produto(109, "Mousepad Speed Extra G", "Acessórios", 89.90, 60, 620),
        Produto(114, "Microfone Condensador", "Áudio", 430.00, 9, 88),
        Produto(118, "Caixa de Som Bluetooth", "Áudio", 260.00, 25, 310),
        Produto(111, "Roteador Wi-Fi 6", "Redes", 390.00, 19, 145),
        Produto(117, "Cabo HDMI 2.1 2m", "Acessórios", 55.00, 80, 750),
        Produto(113, "Suporte Articulado", "Mobiliário", 175.00, 27, 230),
        Produto(116, "Notebook Ultrafino i5", "Computadores", 3490.00, 4, 38),
    ]

def carregar_dados_crescentes():
    """Cenário 2: Já ordenada por código de 101 a 120 (Melhor Caso p/ Insertion/Bubble)"""
    return [
        Produto(101, "Mouse Gamer Wireless", "Periféricos", 220.50, 30, 340),
        Produto(102, "Webcam Full HD", "Vídeo", 189.00, 12, 95),
        Produto(103, "Headset Surround 7.1", "Áudio", 299.90, 22, 210),
        Produto(104, "Hub USB-C 7 em 1", "Acessórios", 145.00, 50, 410),
        Produto(105, "Teclado Mecânico RGB", "Periféricos", 350.00, 15, 120),
        Produto(106, "Fonte 650W 80 Plus", "Hardware", 410.00, 18, 175),
        Produto(107, "Memória RAM 16GB DDR5", "Hardware", 380.00, 35, 290),
        Produto(108, "SSD NVMe 1TB", "Armazenamento", 480.00, 40, 500),
        Produto(109, "Mousepad Speed Extra G", "Acessórios", 89.90, 60, 620),
        Produto(110, "Cadeira Ergonômica", "Mobiliário", 1150.00, 5, 42),
        Produto(111, "Roteador Wi-Fi 6", "Redes", 390.00, 19, 145),
        Produto(112, "Monitor 27' 144Hz", "Monitores", 1450.00, 8, 85),
        Produto(113, "Suporte Articulado", "Mobiliário", 175.00, 27, 230),
        Produto(114, "Microfone Condensador", "Áudio", 430.00, 9, 88),
        Produto(115, "Processador Ryzen 7", "Hardware", 1650.00, 10, 115),
        Produto(116, "Notebook Ultrafino i5", "Computadores", 3490.00, 4, 38),
        Produto(117, "Cabo HDMI 2.1 2m", "Acessórios", 55.00, 80, 750),
        Produto(118, "Caixa de Som Bluetooth", "Áudio", 260.00, 25, 310),
        Produto(119, "Placa de Vídeo RTX 4060", "Hardware", 2199.90, 6, 60),
        Produto(120, "Gabinete Mid Tower", "Hardware", 320.00, 14, 130),
    ]

def carregar_dados_decrescentes():
    """Cenário 3: Inversamente ordenada por código de 120 a 101 (Pior Caso)"""
    crescente = carregar_dados_crescentes()
    decrescente = []
    for i in range(len(crescente) - 1, -1, -1):
        decrescente.append(crescente[i])
    return decrescente