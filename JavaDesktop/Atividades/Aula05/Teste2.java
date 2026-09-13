public class Teste2 {
    public static void main(String[] args) {
        int a = Teclado.leInt("Digite a: ");
        int b = Teclado.leInt("Digite b: ");
        int c = Teclado.leInt("Digite c: ");

        int guarda;
        boolean result1, result2, result3;
        result3 = true;

        if (a < b) {
            guarda = a;
            a = b;
            b = guarda;
            result1 = true;
        } else {
            result1 = false;
        }

        System.out.println("If a menor do que b: " + result1);

        if (b < c) {
            guarda = b;
            b = c;
            c = guarda;
            result2 = false;

            if (a < b) {
                guarda = a;
                a = b;
                b = guarda;
                result3 = false;
            } else {
                result3 = true;
            }
        } else {
            result2 = true;
        }

        System.out.println("If b<c: " + result2);
        System.out.println("If a<b: " + result3);
        System.out.println("Ordem decrescente: " + a + ", " + b + ", " + c);
    }
}
