public class Cofrinho {
    private Pessoa dono; // Dono do cofrinho (do tipo Pessoa)
    private int qt50; // Quantidade de moedas de 10 centavos
    private int qt25; // Quantidade de moedas de 25 centavos
    private int qt10; // Quantidade de moedas de 50 centavos

    // Construtor da classe Cofrinho - Inicializa um cofrinho vazio
    public Cofrinho(Pessoa dono) {
        this.dono = dono;
        this.qt50 = 0;
        this.qt25 = 0;
        this.qt10 = 0;
    }

    // Método set para alterar o dono do cofrinho
    public void setDono(Pessoa dono) {
        this.dono = dono;
    }

    // Método get para retornar o dono do cofrinho
    public Pessoa getDono() {
        return dono;
    }

    // Método para depositar uma moeda de 10 centavos
    public void depositaUmaMoedaDezCentavos() {
        qt10 = qt10 + 1;
    }

    // Método para depositar uma moeda de 25 centavos
    public void depositaUmaMoedaVinteCincoCentavos() {
        qt25 = qt25 + 1;
    }

    // Método para depositar uma moeda de 50 centavos
    public void depositaUmaMoedaCinquentaCentavos() {
        qt50 = qt50 + 1;
    }

    // Método para calcular o valor total armazenado no cofrinho em reais
    public double calculaTotal() {
        double total = 0.10 * qt10 + 0.25 * qt25 + 0.50 * qt50;
        return total;
    }
}
