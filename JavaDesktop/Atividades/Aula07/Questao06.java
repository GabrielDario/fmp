public class Questao06 {

    public static void main(String[] args) {
        // a) Declare uma matriz de inteiros, de nome matriz.
        int[][] matriz;

        // b) Instancie uma matriz de inteiros, de 6 linhas e 4 colunas e atribua para a variável matriz, já declarada.
        matriz = new int[6][4];

        // c) Após a instanciação, qual é o valor de matriz[1][3]?
        // Resposta: O valor é 0. 
        // Em Java, quando um array de inteiros (int) é instanciado, todos os seus elementos
        // são automaticamente inicializados com o valor padrão do tipo primitivo int, que é 0.
        System.out.println("c) O valor de matriz[1][3] eh: " + matriz[1][3]);

        // d) Declare uma matriz de double, de nome notas.
        double[][] notas;

        // e) Declare uma matriz de caracteres de nome letras.
        char[][] letras;
    }
}