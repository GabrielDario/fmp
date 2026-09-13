public class Teste6 {
    public static void main(String[] args) {
        int numero = Teclado.leInt("Digite um numero inteiro: ");

        if (numero % 2 == 0)
            System.out.println("Par");
        else
            System.out.println("Impar");
    }
}
