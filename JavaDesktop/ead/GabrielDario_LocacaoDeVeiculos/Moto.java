public class Moto extends Veiculo {

    private int cilindradas;

    public Moto(String modelo, String marca, int ano, String placa, int cilindradas) {
        super(modelo, marca, ano, placa);
        this.cilindradas = cilindradas;
    }

    public int getCilindradas() {
        return cilindradas;
    }

    public void setCilindradas(int cilindradas) {
        this.cilindradas = cilindradas;
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("Tipo: MOTO");
        System.out.println("Modelo: " + getModelo());
        System.out.println("Marca: " + getMarca());
        System.out.println("Ano: " + getAno());
        System.out.println("Placa: " + getPlaca());
        System.out.println("Cilindradas: " + cilindradas + " cc");
    }
}