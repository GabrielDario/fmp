public class Teste9 {
    public static void main(String[] args) {
        int idade = Teclado.leInt("Digite a idade do atleta: ");
        double peso = 0;

        exibirMensagem(idade, peso);
    }

    public static void exibirMensagem(int idade, double peso) {
        if (idade <= 14) {
            System.out.printf("%d anos - Categoria: Infantil%n", idade);
        } else if (idade >= 15 && idade <= 17) {
            peso = Teclado.leDouble("Digite o peso do atleta: ");

            if (peso <= 50)
                System.out.printf("%d anos - Categoria: Juvenil Leve%n", idade);
            else if (peso <= 60)
                System.out.printf("%d anos - Categoria: Juvenil Pesado%n", idade);
            else
                System.out.println("Peso fora das categorias informadas.");
        } else if (idade >= 18 && idade <= 25) {
            peso = Teclado.leDouble("Digite o peso do atleta: ");

            if (peso <= 60)
                System.out.printf("%d anos - Categoria: Senior Leve%n", idade);
            else
                System.out.printf("%d anos - Categoria: Senior Pesado%n", idade);
        } else {
            System.out.printf("%d anos - Categoria: Veterano%n", idade);
        }
    }
}
