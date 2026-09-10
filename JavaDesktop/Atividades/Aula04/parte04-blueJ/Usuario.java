public abstract class Usuario implements Autenticavel {
    // Encapsulamento: atributos privados
    private int matricula;
    private String nome;
    private String login;
    private String senha;

    public Usuario(int matricula, String nome, String login, String senha) {
        this.matricula = matricula;
        this.nome = nome;
        this.login = login;
        this.senha = senha;
    }

    // Getters e Setters
    public int getMatricula() {
        return this.matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getLogin() {
        return this.login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getSenha() {
        return this.senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }


    @Override
    public boolean autenticar(String login, String senha) {
        return this.login.equals(login) && this.senha.equals(senha);
    }

    public void exibeDados() {
        System.out.println("Matricula: " + matricula);
        System.out.println("Nome: " + nome);
        System.out.println("Login: " + login);
    }
}