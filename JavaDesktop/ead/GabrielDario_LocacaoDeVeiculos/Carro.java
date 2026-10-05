public class Carro extends Veiculo {

    private int nPortas;

    public Carro(String modelo, String marca, int ano, String placa, int nPortas) {
        super(modelo, marca, ano, placa);
        this.nPortas = nPortas;
    }

    public int getnPortas() {
        return nPortas;
    }

    public void setnPortas(int nPortas) {
        this.nPortas = nPortas;
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("Tipo: CARRO");
        System.out.println("Modelo: " + getModelo());
        System.out.println("Marca: " + getMarca());
        System.out.println("Ano: " + getAno());
        System.out.println("Placa: " + getPlaca());
        System.out.println("Número de portas: " + nPortas);
    }
}