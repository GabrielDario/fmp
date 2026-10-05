public class Locacao {

    private Veiculo veiculo;
    private Cliente cliente;
    private Empresa empresa;
    private int dias;

    public Locacao(Veiculo veiculo, Cliente cliente, int dias) {
        this.veiculo = veiculo;
        this.cliente = cliente;
        this.dias = dias;
    }

    public Locacao(Veiculo veiculo, Empresa empresa, int dias) {
        this.veiculo = veiculo;
        this.empresa = empresa;
        this.dias = dias;
    }

    public Veiculo getVeiculo() {
        return veiculo;
    }

    public int getDias() {
        return dias;
    }

    public void exibirLocacao() {

        System.out.println("Veículo: " + veiculo.getModelo());
        System.out.println("Placa: " + veiculo.getPlaca());

        if (cliente != null) {
            System.out.println("Cliente: " + cliente.getNome());
        }

        if (empresa != null) {
            System.out.println("Empresa: " + empresa.getRazaoSocial());
        }

        System.out.println("Prazo: " + dias + " dias");
    }
}