public class Locadora {

    // ARRAY UNIDIMENSIONAL
    private Veiculo[] veiculos;

    private Cliente[] clientes;

    private Locacao[] locacoes;

    private int quantidadeVeiculos;
    private int quantidadeClientes;
    private int quantidadeLocacoes;

    // ARRAY BIDIMENSIONAL
    // linha = cliente
    // coluna = veículo
    private int[][] historicoLocacoes;

    public Locadora() {

        veiculos = new Veiculo[20];
        clientes = new Cliente[20];
        locacoes = new Locacao[100];

        historicoLocacoes = new int[20][20];

        quantidadeVeiculos = 0;
        quantidadeClientes = 0;
        quantidadeLocacoes = 0;
    }

    // CADASTRAR VEÍCULO

    public boolean cadastrarVeiculo(Veiculo veiculo) {

        if (quantidadeVeiculos >= 20) {
            System.out.println("Capacidade máxima de 20 veículos atingida!");
            return false;
        }

        veiculos[quantidadeVeiculos] = veiculo;
        quantidadeVeiculos++;

        System.out.println("Veículo cadastrado com sucesso!");

        return true;
    }

    // CADASTRAR CLIENTE

    public boolean cadastrarCliente(Cliente cliente) {
        if (quantidadeClientes >= 20) {
            System.out.println("Capacidade máxima de clientes atingida!");
            return false;
        }
        clientes[quantidadeClientes] = cliente;
        quantidadeClientes++;
        System.out.println("Cliente cadastrado com sucesso!");
        return true;
    }
    // LISTAR VEÍCULOS

    public void listarVeiculos() {

        if (quantidadeVeiculos == 0) {
            System.out.println("Nenhum veículo cadastrado.");
            return;
        }

        for (int i = 0; i < quantidadeVeiculos; i++) {

            System.out.println("\n==========================");
            System.out.println("Número: " + (i + 1));

            veiculos[i].exibirInformacoes();

            if (veiculos[i].isDisponivel()) {
                System.out.println("Status: DISPONÍVEL");
            } else {
                System.out.println("Status: ALUGADO");
            }
        }
    }

    // LISTAR SOMENTE DISPONÍVEIS
    public void listarVeiculosDisponiveis() {
        System.out.println("\n===== VEÍCULOS DISPONÍVEIS =====");
        for (int i = 0; i < quantidadeVeiculos; i++) {
            if (veiculos[i].isDisponivel()) {
                veiculos[i].exibirDetalhes();
                System.out.println("--------------------------");
            }
        }
    }

    public void realizarLocacao(Veiculo veiculo, Cliente cliente) {
        realizarLocacao(veiculo, cliente, 7);
    }

    public void realizarLocacao(Veiculo veiculo, Empresa empresa) {
        if (!veiculo.isDisponivel()) {
            System.out.println("Veículo já está alugado!");
            return;
        }
        veiculo.setDisponivel(false);
        Locacao locacao = new Locacao(veiculo, empresa, 15);
        locacoes[quantidadeLocacoes] = locacao;
        quantidadeLocacoes++;
        System.out.println("Locação para empresa realizada!");
        System.out.println("Prazo: 15 dias");
    }

    public void realizarLocacao(Veiculo veiculo, Cliente cliente, int dias) {

        if (!veiculo.isDisponivel()) {
            System.out.println("Veículo já está alugado!");
            return;
        }
        veiculo.setDisponivel(false);
        cliente.adicionarVeiculo(veiculo);
        Locacao locacao = new Locacao(veiculo, cliente, dias);
        locacoes[quantidadeLocacoes] = locacao;
        quantidadeLocacoes++;

        // Histórico
        int indiceCliente = buscarCliente(cliente);
        int indiceVeiculo = buscarVeiculo(veiculo);

        if (indiceCliente != -1 && indiceVeiculo != -1) {
            historicoLocacoes[indiceCliente][indiceVeiculo] = 1;
        }

        System.out.println("Locação realizada com sucesso!");
        System.out.println("Prazo: " + dias + " dias");
    }

    // BUSCAR CLIENTE
    private int buscarCliente(Cliente cliente) {
        for (int i = 0; i < quantidadeClientes; i++) {
            if (clientes[i] == cliente) {
                return i;
            }
        }
        return -1;
    }

    // BUSCAR VEÍCULO
    private int buscarVeiculo(Veiculo veiculo) {
        for (int i = 0; i < quantidadeVeiculos; i++) {
            if (veiculos[i] == veiculo) {
                return i;
            }
        }

        return -1;
    }

    // DEVOLUÇÃO
    public void devolverVeiculo(Veiculo veiculo, Cliente cliente) {
        if (veiculo.isDisponivel()) {
            System.out.println("Este veículo não está alugado.");
            return;
        }
        veiculo.setDisponivel(true);
        cliente.removerVeiculo(veiculo);
        System.out.println("Veículo devolvido com sucesso!");
    }

    // VEÍCULOS ALUGADOS
    public void listarVeiculosAlugados() {
        System.out.println("\n===== VEÍCULOS ALUGADOS =====");
        boolean encontrou = false;
        for (int i = 0; i < quantidadeVeiculos; i++) {
            if (!veiculos[i].isDisponivel()) {
                veiculos[i].exibirDetalhes();
                System.out.println("-----------------------");
                encontrou = true;
            }
        }
        if (!encontrou) {
            System.out.println("Nenhum veículo alugado.");
        }
    }

    public void exibirHistorico() {
        System.out.println("\n===== HISTÓRICO DE LOCAÇÕES =====");
        for (int i = 0; i < quantidadeClientes; i++) {
            System.out.println("\nCliente: " + clientes[i].getNome());
            for (int j = 0; j < quantidadeVeiculos; j++) {
                if (historicoLocacoes[i][j] == 1) {

                    System.out.println(
                            "Alugou: "
                                    + veiculos[j].getModelo()
                                    + " - "
                                    + veiculos[j].getPlaca());
                }
            }
        }
    }

    // CALCULAR MULTA
    public double calcularMulta(int dias, Veiculo veiculo) {
        double valorPorDia;
        if (veiculo instanceof Carro) {
            valorPorDia = 50.00;
        } else if (veiculo instanceof Moto) {
            valorPorDia = 30.00;
        } else if (veiculo instanceof Caminhao) {
            valorPorDia = 100.00;
        } else {
            valorPorDia = 0.00;
        }
        return dias * valorPorDia;
    }

    // LISTAR CLIENTES
    public void listarClientes() {
        System.out.println("\n===== CLIENTES =====");
        for (int i = 0; i < quantidadeClientes; i++) {
            System.out.println("Número: " + (i + 1));
            System.out.println("Nome: " + clientes[i].getNome());
            System.out.println("CPF: " + clientes[i].getCpf());
            System.out.println("Idade: " + clientes[i].getIdade());
            System.out.println("-------------------");
        }
    }

    public Cliente getCliente(int indice) {
        if (indice >= 0 && indice < quantidadeClientes) {
            return clientes[indice];
        }
        return null;
    }

    public Veiculo getVeiculo(int indice) {
        if (indice >= 0 && indice < quantidadeVeiculos) {
            return veiculos[indice];
        }
        return null;
    }

    public int getQuantidadeClientes() {
        return quantidadeClientes;
    }

    public int getQuantidadeVeiculos() {
        return quantidadeVeiculos;
    }
}