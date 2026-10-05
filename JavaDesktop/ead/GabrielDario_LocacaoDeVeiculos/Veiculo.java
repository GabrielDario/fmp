public class Veiculo {

    private String modelo;
    private String marca;
    private int ano;
    private String placa;
    private boolean disponivel;

    public Veiculo(String modelo, String marca, int ano, String placa) {
        this.modelo = modelo;
        this.marca = marca;
        this.ano = ano;
        this.placa = placa;
        this.disponivel = true;
    }

    // Getters e Setters

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public boolean isDisponivel() {
        return disponivel;
    }

    public void setDisponivel(boolean disponivel) {
        this.disponivel = disponivel;
    }

    // Método que poderá ser sobrescrito
    public void exibirInformacoes() {
        System.out.println("Modelo: " + modelo);
        System.out.println("Marca: " + marca);
        System.out.println("Ano: " + ano);
        System.out.println("Placa: " + placa);
    }

    // Exibe detalhes gerais do veículo
    public void exibirDetalhes() {
        exibirInformacoes();

        if (disponivel) {
            System.out.println("Status: DISPONÍVEL");
        } else {
            System.out.println("Status: ALUGADO");
        }
    }
}