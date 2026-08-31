public class Pedido {
    private Cliente cliente;
    private Computador computador;
    private Monitor monitor;

    // Construtor
    public Pedido(Cliente cliente) {
        this.cliente = cliente;
    }

    // Getters e Setters
    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public Computador getComputador() {
        return computador;
    }

    public void setComputador(Computador computador) {
        this.computador = computador;
    }

    public Monitor getMonitor() {
        return monitor;
    }

    public void setMonitor(Monitor monitor) {
        this.monitor = monitor;
    }

    // Método para adicionar um Computador ao pedido
    public void adicionarComputador(Computador computador) {
        this.computador = computador;
    }

    // Método para adicionar um Monitor ao pedido
    public void adicionarMonitor(Monitor monitor) {
        this.monitor = monitor;
    }

    // Método para calcular o valor total do pedido
    public double calcularValorTotal() {
        double valorTotal = 0.0;
        if (computador != null) {
            valorTotal += computador.getPreco();
        }
        if (monitor != null) {
            valorTotal += monitor.getPreco();
        }
        return valorTotal;
    }
}
