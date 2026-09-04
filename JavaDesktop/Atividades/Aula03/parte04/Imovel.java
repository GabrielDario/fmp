public class Imovel {
    // Atributos
    private int codigo;
    private String descricao;
    private double precoAluguel;
    private int qtdMinimaMeses;

    // Construtor
    public Imovel(int codigo, String descricao, double precoAluguel, int qtdMinimaMeses) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.precoAluguel = precoAluguel;
        this.qtdMinimaMeses = qtdMinimaMeses;
    }

    public int getCodigo() {
        return codigo;
    }

    public String getDescricao() {
        return descricao;
    }

    public double getPrecoAluguel() {
        return precoAluguel;
    }

    public int getQtdMinimaMeses() {
        return qtdMinimaMeses;
    }
    

    public void exibeDados() {
        System.out.println("--- DADOS DO IMÓVEL ---");
        System.out.println("Código: " + codigo);
        System.out.println("Descrição: " + descricao);
        System.out.printf("Preço Aluguel: R$ %.2f\n", precoAluguel);
        System.out.println("Qtd. Mínima de Meses: " + qtdMinimaMeses);
    }
}