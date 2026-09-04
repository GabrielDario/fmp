public class TesteAluguel {
    public static void main(String[] args) {
        System.out.println("=== CADASTRO DE CLIENTE ===");
        int codCliente = Teclado.leInt("Código do cliente: ");
        String nomeCliente = Teclado.leString("Nome do cliente: ");
        String telCliente = Teclado.leString("Telefone do cliente: ");
        
        Cliente cliente = new Cliente(codCliente, nomeCliente, telCliente);

        System.out.println("\n=== CADASTRO DE IMÓVEL ===");
        int codImovel = Teclado.leInt("Código do imóvel: ");
        String descImovel = Teclado.leString("Descrição do imóvel: ");
        double precoImovel = Teclado.leDouble("Preço do aluguel: ");
        int qtdMeses = Teclado.leInt("Quantidade mínima de meses: ");

        Imovel imovel = new Imovel(codImovel, descImovel, precoImovel, qtdMeses);

        System.out.println("\n=== REGISTRO DE ALUGUEL ===");
        int codAluguel = Teclado.leInt("Código do aluguel: ");
        String dataInicio = Teclado.leString("Data de início (DD/MM/AAAA): ");
        String dataFim = Teclado.leString("Data de fim (DD/MM/AAAA): ");

        // Associação das instâncias de Cliente e Imovel na classe Aluguel
        Aluguel aluguel = new Aluguel(codAluguel, dataInicio, dataFim, imovel, cliente);

        System.out.println("\n");
        // Exibição completa utilizando o método exibeDados()
        aluguel.exibeDados();
    }
}