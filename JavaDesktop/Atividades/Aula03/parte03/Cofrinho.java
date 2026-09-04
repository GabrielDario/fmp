public class Cofrinho {
    private Pessoa dono; // Dono do cofrinho (do tipo Pessoa)
    private int qt50; // Quantidade de moedas de 10 centavos
    private int qt25; // Quantidade de moedas de 25 centavos
    private int qt10; // Quantidade de moedas de 50 centavos

    public Cofrinho(Pessoa dono) {
        this.dono = dono;
        this.qt50 = 0;
        this.qt25 = 0;
        this.qt10 = 0;
    }

    public void setDono(Pessoa dono) {
        this.dono = dono;
    }

    public Pessoa getDono() {
        return dono;
    }

    public void depositaUmaMoedaDezCentavos() {
        qt10 = qt10 + 1;
    }

    public void depositaUmaMoedaVinteCincoCentavos() {
        qt25 = qt25 + 1;
    }

    public void depositaUmaMoedaCinquentaCentavos() {
        qt50 = qt50 + 1;
    }

    public double calculaTotal() {
        double total = 0.10 * qt10 + 0.25 * qt25 + 0.50 * qt50;
        return total;
    }
}
