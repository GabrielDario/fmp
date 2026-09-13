public class Teste5 {
    public static void main(String[] args) {
        int numero = Teclado.leInt("Digite um numero: ");

        if (numero < 0)
            System.out.println("Negativo");
        else
            System.out.println("Nao negativo");
    }
}
