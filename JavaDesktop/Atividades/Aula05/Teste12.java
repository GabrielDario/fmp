public class Teste12 {
    public static void main(String[] args) {
        int ano = Teclado.leInt("Digite o ano: ");

        boolean bissexto;

        if (ano % 4 == 0 && (ano % 100 != 0 || ano % 400 == 0))
            bissexto = true;
        else
            bissexto = false;

        if (bissexto)
            System.out.println("O ano " + ano + " e bissexto.");
        else
            System.out.println("O ano " + ano + " nao e bissexto.");

        int mes = Teclado.leInt("Digite o numero do mes (1 a 12): ");

        int dias;

        switch (mes) {
            case 2:
                dias = bissexto ? 29 : 28;
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                dias = 30;
                break;
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                dias = 31;
                break;
            default:
                dias = 0;
        }

        if (dias == 0)
            System.out.println("Mes invalido.");
        else
            System.out.println("O mes possui " + dias + " dias.");
    }
}
