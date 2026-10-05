public class Questao08 {

    public static void main(String[] args) {
        Questao08 array = new Questao08(); // instancia um objeto
        int[][] matriz = new int[2][2];
        double temp = array.calculaMedia(matriz);

        System.out.println("\nA media eh " + temp);
    }

    public double calculaMedia(int[][] matriz) {
        int count = 0;
        double media = 0;
        double soma = 0;
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = Teclado.leInt("Digite um numero: ");
                soma = soma + matriz[i][j];
                count++;
            }
        }
        return soma / count;
    }
}