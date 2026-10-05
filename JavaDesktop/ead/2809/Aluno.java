public class Aluno {

    private int codigo;
    private String nome;
    private String dataNascimento;
    private String email;
    private String senha;
    private Curso curso;
    private double[] notas = new double[3];
    private boolean[] notaLancada = new boolean[3];

    public Curso getCurso() {
        return curso;
    }

    public void setCurso(Curso curso) {
        this.curso = curso;
    }

    public Aluno(int codigo, String nome, String dataNascimento,
            String email, String senha) {

        this.codigo = codigo;
        this.nome = nome;
        this.dataNascimento = dataNascimento;
        this.email = email;
        this.senha = senha;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDataNascimento() {
        return dataNascimento;
    }

    public void setDataNascimento(String dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public void exibeDados() {
        System.out.println("Código: " + codigo);
        System.out.println("Nome: " + nome);
        System.out.println("Data de nascimento: " + dataNascimento);
        System.out.println("E-mail: " + email);

        Aluno aluno = new Aluno(1, "João", "10/05/2000",
                "joao@email.com", "1234");

        Curso curso = new Curso(101, "Análise e Desenvolvimento de Sistemas", 5);

        aluno.setCurso(curso);
    }

    public void lancarNota(int indice, double nota) {

        if (indice >= 0 && indice < 3) {

            notas[indice] = nota;
            notaLancada[indice] = true;

        } else {
            System.out.println("Índice de nota inválido.");
        }
    }

    public double calcularMedia() {

        double soma = 0;
        int quantidadeNotas = 0;

        for (int i = 0; i < 3; i++) {

            if (notaLancada[i]) {
                soma += notas[i];
                quantidadeNotas++;
            }
        }

        if (quantidadeNotas == 0) {
            return 0;
        }

        return soma / quantidadeNotas;
    }

    public void exibirNotas() {

    System.out.println("Aluno: " + nome);

    for (int i = 0; i < 3; i++) {

        if (notaLancada[i]) {
            System.out.println("Nota " + (i + 1) + ": " + notas[i]);
        } else {
            System.out.println("Nota " + (i + 1) + ": Não lançada");
        }
    }

    System.out.println("Média: " + calcularMedia());
}
}