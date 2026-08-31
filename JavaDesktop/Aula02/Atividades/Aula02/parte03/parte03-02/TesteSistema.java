public class TesteSistema {
    public static void main(String[] args) {
        // Criando um cliente
        Cliente cliente = new Cliente("João Silva", "123.456.789-00");

        // Criando um computador
        Computador computador = new Computador("Inspiron", "Dell", 3500.00);

        // Criando um monitor
        Monitor monitor = new Monitor("UltraSharp", "Dell", 800.00);

        // Criando um pedido e associando o cliente
        Pedido pedido = new Pedido(cliente);

        // Adicionando o computador ao pedido
        pedido.adicionarComputador(computador);

        // Adicionando o monitor ao pedido
        pedido.adicionarMonitor(monitor);

        // Exibindo as informações do pedido
        System.out.println("Cliente: " + pedido.getCliente().getNome());
        System.out.println("Computador: " + pedido.getComputador().getModelo() + " - R$ " + pedido.getComputador().getPreco());
        System.out.println("Monitor: " + pedido.getMonitor().getModelo() + " - R$ " + pedido.getMonitor().getPreco());
        System.out.println("Valor Total do Pedido: R$ " + pedido.calcularValorTotal());
    }
}
