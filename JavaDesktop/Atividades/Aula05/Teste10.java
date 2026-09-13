public class Teste10 {
    public static void main(String[] args) {
        int numUm = Teclado.leInt("Digite o primeiro numero: ");
        int outroNum = Teclado.leInt("Digite o segundo numero: ");

        if (numUm != outroNum)
            System.out.println("Os dois sao diferentes");
        else
            System.out.println("Os dois sao iguais");
    }
}
