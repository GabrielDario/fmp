import java.io.*;

public class Teclado {
    private static String s;
    private static InputStreamReader i = new InputStreamReader(System.in);
    private static BufferedReader d = new BufferedReader(i);

    public static int leInt(String msg) {
        int a = 0;
        System.out.print(msg);
        try {
            s = d.readLine();
            a = Integer.parseInt(s);
        } catch (IOException e) {
            System.out.println("Erro de I/O: " + e);
        } catch (NumberFormatException e) {
            System.out.println("O valor digitado deve ser inteiro: " + e);
        }
        return a;
    }

    public static double leDouble(String msg) {
        double a = 0;
        System.out.print(msg);
        try {
            s = d.readLine();
            a = Double.parseDouble(s);
        } catch (IOException e) {
            System.out.println("Erro de I/O: " + e);
        } catch (NumberFormatException e) {
            System.out.println("O valor digitado deve ser numero: " + e);
        }
        return a;
    }

    public static String leString(String msg) {
        s = "";
        System.out.print(msg);
        try {
            s = d.readLine();
        } catch (IOException e) {
            System.out.println("Erro de I/O: " + e);
        }
        return s;
    }

    public static Character leChar(String msg) {
        s = "";
        System.out.print(msg);
        try {
            s = d.readLine();
        } catch (IOException e) {
            System.out.println("Erro de I/O: " + e);
        }
        return s.charAt(0);
    }
}
