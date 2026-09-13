public class Teste8 {
    public static void main(String[] args) {
        String nome1 = Teclado.leString("Digite o nome da primeira pessoa: ");
        int idade1 = Teclado.leInt("Digite a idade da primeira pessoa: ");

        String nome2 = Teclado.leString("Digite o nome da segunda pessoa: ");
        int idade2 = Teclado.leInt("Digite a idade da segunda pessoa: ");

        Pessoa p1 = new Pessoa(nome1, idade1);
        Pessoa p2 = new Pessoa(nome2, idade2);

        p1.exibeDados();
        p2.exibeDados();

        if (nome1.equals(nome2))
            System.out.println("Os nomes sao iguais.");
        else
            System.out.println("Os nomes sao diferentes.");
    }
}
