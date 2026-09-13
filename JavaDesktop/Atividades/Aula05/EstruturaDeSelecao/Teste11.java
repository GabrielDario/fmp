public class Teste11 {
    public static void main(String[] args) {
        int idade = Teclado.leInt("Digite a idade da pessoa: ");

        String msg;

        if (idade <= 13)
            msg = "Infantil";
        else if (idade <= 18)
            msg = "Adolescente";
        else if (idade < 25)
            msg = "Jovem";
        else if (idade <= 70)
            msg = "Adulto";
        else
            msg = "Terceira idade";

        System.out.println("Classificacao: " + msg);
    }
}
