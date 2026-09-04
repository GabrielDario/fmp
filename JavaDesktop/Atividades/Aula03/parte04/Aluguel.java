public class Aluguel {
    // Atributos
    private int codigo;
    private String dataInicio;
    private String dataFim;
    private Imovel imovel;
    private Cliente cliente;

    // Construtor
    public Aluguel(int codigo, String dataInicio, String dataFim, Imovel imovel, Cliente cliente) {
        this.codigo = codigo;
        this.dataInicio = dataInicio;
        this.dataFim = dataFim;
        this.imovel = imovel;
        this.cliente = cliente;
    }

    // Getters auxiliares
    public int getCodigo() {
        return codigo;
    }

    public String getDataInicio() {
        return dataInicio;
    }

    public String getDataFim() {
        return dataFim;
    }

    public Imovel getImovel() {
        return imovel;
    }

    public Cliente getCliente() {
        return cliente;
    }
    
    // Método para exibir todos os dados do contrato de aluguel
    public void exibeDados() {
        System.out.println("====================================");
        System.out.println("       CONTRATO DE ALUGUEL          ");
        System.out.println("====================================");
        System.out.println("Código do Aluguel: " + codigo);
        System.out.println("Data de Início: " + dataInicio);
        System.out.println("Data de Fim: " + dataFim);
        System.out.println();
        
        // Chamada dos métodos exibeDados() dos objetos associados
        cliente.exibeDados();
        System.out.println();
        imovel.exibeDados();
        System.out.println("====================================");
    }
}