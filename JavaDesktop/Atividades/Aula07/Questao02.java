public class Questao02 {

    public static void main(String[] args) {
        int[] vet;
        
        //System.out.println("b) Valor de vet antes da instanciação: " + vet[0]);
        //NULL NAO EXOSTE

        vet = new int[15];

        System.out.println("d) Valor de vet[5]: " + vet[5]);

        int tam = vet.length;
        System.out.println("e) Valor de tam: " + tam);

        System.out.println("f) Último elemento: vet[14] = " + vet[14]);

        System.out.println("g) Índice do primeiro elemento: 0");

        double[] medias = new double[20];

        System.out.println("h) Tamanho do array medias: " + medias.length);
    }
}