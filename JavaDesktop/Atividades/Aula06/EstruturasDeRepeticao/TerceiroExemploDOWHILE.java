public class TerceiroExemploDOWHILE {
    public static void main(String args[]) {
        double saldo = 600.00;
        char opcao;

        do {
            double retirada = Teclado.leDouble("Informe um valor para retirada: ");
            while (retirada > saldo) {
                System.out.println("Saldo indisponivel para este valor de retirada.");
                retirada = Teclado.leDouble("Informe um novo valor para retirada: ");
            }

            saldo = saldo - retirada;
            System.out.println("Seu novo saldo é: " + saldo);

            opcao = Teclado.leChar("Deseja fazer uma nova operação (S/N): ");

        } while (Character.toLowerCase(opcao) == 's');
    }
}
