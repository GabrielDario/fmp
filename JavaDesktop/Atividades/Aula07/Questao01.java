
public class Questao01 {
    public static void main(String[] args) {

        int[] a = { 507, -15, 147, 2194, 300, 27, 888, -110, 0, 675 };
        int i = 2;

        System.out.println("indice? " + i + "Contem o elemento " + a[i]);
        System.out.println("Terceiro elemento do array é? " + a[2]);
        System.out.println("Primeiro elemento do array é? " + a[1]);
        System.out.println("E qual é o Elemento zero do array ?? " + a[0]);
        a[1] = Teclado.leInt("Informe um número inteiro: ");
        System.out.println("Agora o Elemento 1 é o que vc digitou é igual a " + a[1]);
    }
}