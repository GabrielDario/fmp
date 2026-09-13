public class Teste7 {
    public static void main(String[] args) {
        double a = Teclado.leDouble("Digite o primeiro numero: ");
        double b = Teclado.leDouble("Digite o segundo numero: ");

        if (a > b)
            System.out.println("Maior: " + a);
        else if (b > a)
            System.out.println("Maior: " + b);
        else
            System.out.println("Os dois numeros sao iguais.");
    }
}
