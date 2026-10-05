public class Questao05 {

    public static void main(String[] args) {

        int[][] mat = {
            {13, 45, 12, 19},
            {67, -5, 88, 37},
            {11, 43, 13, 0},
            {64, 52, 29, 18},
            {71, 14, 19, 62}
        };

        // a) Quantas linhas tem a matriz?
        System.out.println("a) Quantidade de linhas: " + mat.length);

        // b) Quantas colunas tem a matriz?
        System.out.println("b) Quantidade de colunas: " + mat[0].length);

        // c) Onde está armazenado o valor 19?
        System.out.println("c) O valor 19 está em:");
        System.out.println("   mat[0][3] = " + mat[0][3]);
        System.out.println("   mat[4][2] = " + mat[4][2]);

        // d) mat[1][1]
        System.out.println("d) mat[1][1] = " + mat[1][1]);

        // e) mat[2][0] + 1
        System.out.println("e) mat[2][0] + 1 = " + (mat[2][0] + 1));

        // f) mat[3+1][3-1]
        System.out.println("f) mat[3+1][3-1] = " + mat[3 + 1][3 - 1]);

        // g) int x = 2; mat[x][x]
        int x = 2;
        System.out.println("g) mat[x][x] = " + mat[x][x]);

        // h) mat[x+1][x]
        System.out.println("h) mat[x+1][x] = " + mat[x + 1][x]);

        // i) mat[x][x] + 1
        System.out.println("i) mat[x][x] + 1 = " + (mat[x][x] + 1));

        // j) mat.length
        System.out.println("j) mat.length = " + mat.length);

        // k) mat[mat.length-1][1]
        System.out.println("k) mat[mat.length-1][1] = "
                + mat[mat.length - 1][1]);

        // l) Quantos números estão armazenados?
        System.out.println("l) Quantidade de números armazenados: "
                + (mat.length * mat[0].length));
    }
}