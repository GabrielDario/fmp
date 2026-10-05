public class Questao04 {

    public static void main(String[] args) {
        Questao04 array = new Questao04(); // instancia um objeto
        int[] notas = new int[3];
        float temp = array.digitaNota(notas);
        System.out.printf("A media eh %.2f", temp);
    }

    public float digitaNota(int[] vet) {

        int soma = 0;
        int count = 0;
        int media = 0;
        for (int i = 0; i < vet.length; i++) {
            vet[i] = Teclado.leInt("Digite uma nota: ");
            if (vet[i] < 0.0 || vet[i] > 10.0) {
                do {
                    System.out.println("Nota inválida!!");
                    vet[i] = Teclado.leInt("\nDigite outra nota: ");
                } while (vet[i] < 0.0 || vet[i] > 10.0);
            }
            soma = soma + vet[i];
            count++;
        }
        return media = soma / count;
    }
}