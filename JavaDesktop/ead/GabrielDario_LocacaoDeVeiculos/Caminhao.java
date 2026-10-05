public class Caminhao extends Veiculo {

    private double cargaMaxima;

    public Caminhao(String modelo, String marca, int ano, String placa, double cargaMaxima) {
        super(modelo, marca, ano, placa);
        this.cargaMaxima = cargaMaxima;
    }

    public double getCargaMaxima() {
        return cargaMaxima;
    }

    public void setCargaMaxima(double cargaMaxima) {
        this.cargaMaxima = cargaMaxima;
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("Tipo: CAMINHÃO");
        System.out.println("Modelo: " + getModelo());
        System.out.println("Marca: " + getMarca());
        System.out.println("Ano: " + getAno());
        System.out.println("Placa: " + getPlaca());
        System.out.println("Carga máxima: " + cargaMaxima + " toneladas");
    }
}