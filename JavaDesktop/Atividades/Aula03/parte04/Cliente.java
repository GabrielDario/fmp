public class Cliente {
    // Atributos
    private int codigo;
    private String nome;
    private String telefone;

    // Construtor
    public Cliente(int codigo, String nome, String telefone) {
        this.codigo = codigo;
        this.nome = nome;
        this.telefone = telefone;
    }

    // Métodos de Acesso
    public String getNome() {
        return nome;
    }

    public String getTelefone() {
        return telefone;
    }

    public int getCodigo() {
        return codigo;
    }
    public void exibeDados() {
        System.out.println("--- DADOS DO CLIENTE ---");
        System.out.println("Código: " + codigo);
        System.out.println("Nome: " + nome);
        System.out.println("Telefone: " + telefone);
    }
    
}