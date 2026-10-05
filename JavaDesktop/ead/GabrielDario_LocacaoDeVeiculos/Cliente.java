public class Cliente {

    private String nome;
    private String cpf;
    private int idade;

    private Veiculo[] veiculosAlugados;
    private int quantidadeVeiculos;

    public Cliente(String nome, String cpf, int idade) {
        this.nome = nome;
        this.cpf = cpf;
        this.idade = idade;

        veiculosAlugados = new Veiculo[20];
        quantidadeVeiculos = 0;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void adicionarVeiculo(Veiculo veiculo) {

        if (quantidadeVeiculos < veiculosAlugados.length) {
            veiculosAlugados[quantidadeVeiculos] = veiculo;
            quantidadeVeiculos++;
        }
    }

    public void removerVeiculo(Veiculo veiculo) {

        for (int i = 0; i < quantidadeVeiculos; i++) {

            if (veiculosAlugados[i] == veiculo) {

                for (int j = i; j < quantidadeVeiculos - 1; j++) {
                    veiculosAlugados[j] = veiculosAlugados[j + 1];
                }

                veiculosAlugados[quantidadeVeiculos - 1] = null;
                quantidadeVeiculos--;

                break;
            }
        }
    }

    public void listarVeiculosAlugados() {

        System.out.println("Veículos alugados por " + nome + ":");

        if (quantidadeVeiculos == 0) {
            System.out.println("Nenhum veículo alugado.");
            return;
        }

        for (int i = 0; i < quantidadeVeiculos; i++) {
            veiculosAlugados[i].exibirDetalhes();
            System.out.println("-------------------------");
        }
    }
}