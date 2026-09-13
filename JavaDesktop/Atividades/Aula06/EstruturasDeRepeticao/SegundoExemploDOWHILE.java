public class SegundoExemploDOWHILE {
    public static void main(String args[]) {
        double saldo = 600.00;

        double retirada = Teclado.leDouble("Informe um valor para retirada: ");

        do {
            System.out.println("Saldo indisponivel para este valor de retirada.");
            retirada = Teclado.leDouble("Informe um novo valor para retirada: ");
        } while (retirada > saldo);

        saldo = saldo - retirada;

        System.out.println("Seu novo saldo é: " + saldo);
    }
}
