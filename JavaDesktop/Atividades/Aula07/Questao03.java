public class Questao03 {

    public static void main(String[] args) {

        Questao03 questao03 = new Questao03(); // instancia o objeto
        double[] notas = new double[3];
        double temp = questao03.digitaNota(notas);

        // invoca método a partir de um objeto e passa um parâmetro
        // já salvando o retorno numa variável temp
        System.out.print("A média eh " + temp);
    }

    public double digitaNota(double[] vet) {
        // método exige um parâmetro do tipo int
        double soma = 0;
        int count = 0;
        double media = 0;

        for (int i = 0; i < vet.length; i++) {

            vet[i] = Teclado.leDouble("Digite uma nota: ");

            if (vet[i] < 0.0 || vet[i] > 10.0) {
                do {
                    System.out.println("Nota inválida!!");
                    vet[i] = Teclado.leDouble("Digite outra nota: ");
                }
                while (vet[i] < 0.0 || vet[i] > 10.0);
            }

            soma = soma + vet[i];
            count++;
        }

        return media = soma / count;
    }
}