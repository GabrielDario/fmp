public class Questao07 {

    public static void main(String[] args) {
        Questao07 array = new Questao07(); // instancia um objeto
        int[][] matriz = new int[5][5];
        int temp = array.impares(matriz);
        System.out.print("\nA qtd de impares eh " + temp);
    }

    public int impares(int[][] matriz) {
        int count = 0;
        int x = 0;

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                if (x % 2 == 1) {
                    matriz[i][j] = x;
                    System.out.println(" " + matriz[i][j]);
                    count++;
                }
                x++;
            }
        }
        return count;
    }
}