public class Teste4 {
    public static void main(String[] args) {
        int idade = Teclado.leInt("Digite a idade: ");
        double preco = Teclado.leDouble("Digite o preco normal: ");

        double precoFinal;

        if (idade <=    12) {
            precoFinal = preco * 0.50;
        } else if (idade <= 17) {
            precoFinal = preco * 0.75;
        } else {
            precoFinal = preco;
        }

        System.out.println("Escolha a categoria pelo menu:");
        System.out.println("1 - Infantil");
        System.out.println("2 - Juvenil");
        System.out.println("3 - Adulto");

        int opcao = Teclado.leInt("Digite a opcao: ");

        switch (opcao) {
            case 1:
                System.out.println("Categoria: Infantil");
                break;
            case 2:
                System.out.println("Categoria: Juvenil");
                break;
            case 3:
                System.out.println("Categoria: Adulto");
                break;
            default:
                System.out.println("Categoria invalida.");
        }

        System.out.printf("Preco final: R$ %.2f%n", precoFinal);
    }
}
