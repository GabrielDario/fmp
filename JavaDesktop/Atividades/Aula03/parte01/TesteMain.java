import java.util.Scanner;

public class TesteMain {
    public static void main(String[] args) {
        // --- 1. Entrada de dados usando a sua classe TECLADO ---
        System.out.println("=== Entrada com a classe TECLADO ===");
        String nomeTeclado = Teclado.leString("Digite seu nome: ");
        int idadeTeclado = Teclado.leInt("Digite sua idade: ");
        double alturaTeclado = Teclado.leDouble("Digite sua altura (ex: 1.75): ");
        char generoTeclado = Teclado.leChar("Digite seu gênero (M/F): ");

        // --- 2. Entrada de dados usando a classe SCANNER ---
        System.out.println("\n=== Entrada com a classe SCANNER ===");
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o nome da sua cidade: ");
        String cidade = scanner.nextLine();

        System.out.print("Digite a quantidade de irmãos: ");
        int irmaos = scanner.nextInt();

        System.out.print("Digite o peso (ex: 70.5): ");
        double peso = scanner.nextDouble();

        System.out.print("É estudante? (true/false): ");
        boolean estudante = scanner.nextBoolean();

        scanner.close(); 

        System.out.println("\n=== Saída Formatada de Dados ===");
        
        System.out.printf("Nome: %s\n", nomeTeclado);
        System.out.printf("Idade: %d anos\n", idadeTeclado);
        System.out.printf("Altura: %.2f m\n", alturaTeclado); // %.2f limita a 2 casas decimais
        System.out.printf("Gênero: %c\n", generoTeclado);
        System.out.printf("Cidade: %s\n", cidade);
        System.out.printf("Número de Irmãos: %d\n", irmaos);
        System.out.printf("Peso: %.1f kg\n", peso);
        System.out.printf("Situação de Estudante: %b\n", estudante);

        System.out.printf("\nResumo: %s (%c) tem %d anos, mora em %s e status de estudante = %b.\n",
                nomeTeclado, generoTeclado, idadeTeclado, cidade, estudante);
    }
}