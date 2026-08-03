

public class Pessoa
{
    private String nome;
    private int idade;
    
    public Pessoa(String nome, int idade)
    {
        this.nome = nome;
        this.idade = idade;
    }
 
    public void fazAniversario() {
    this.idade = this.idade + 1;
}
    
    public void exibeDados(){
        System.out.println("O nome da pessoa é " + nome);
        System.out.println("A idade da pessoa é "    + idade);
    }
}