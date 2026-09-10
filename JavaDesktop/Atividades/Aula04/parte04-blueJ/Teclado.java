import java.io.*;

/** Classe que permite fazer leitura de dados do teclado, com métodos estáticos.
 *  Iso significa que não há necessidade de instanciar um objeto para invocar os métodos.
 *  Sintaxe p/ chamada: <nome_da_classe>.<nome_do_método>(<mensagem de solicitação>)
 *  Exemplo de chamada: Teclado.leInt("Digite um número inteiro")
 */ 

public class Teclado
{
     private static String s;
     private static InputStreamReader i = new InputStreamReader (System.in);
     private static BufferedReader d = new BufferedReader(i);

     
     /**
        Lê um inteiro, exibindo na tela uma mensagem de solicitação.
        @return int
     */
     public static int leInt (String msg)
     {   int a = 0;
         System.out.print(msg);
         try
         {
             s = d.readLine();
             a = Integer.parseInt(s);
         }
         catch (IOException e)
         {
             System.out.println ("Erro de I/O: "+e );
         }
         catch (NumberFormatException e)
         {
             System.out.println ("o valor digitado deve ser inteiro: "+e );
         }
         return (a);
     }
     
     /**
        Lê um double, exibindo na tela uma mensagem de solicitação.
        @return double
     */
     public static double leDouble(String msg)
     {   double a = 0;
         System.out.print(msg);
         try
         {
             s = d.readLine();
             a = Double.parseDouble(s);
         }
         catch (IOException e)
         {
             System.out.println ("Erro de I/O: " + e);
         }
         catch (NumberFormatException e)
         {
             System.out.println ("o valor digitado deve ser numero: "+e );
         }
         return (a);
     }
     
     /**
        Lê um string, exibindo na tela uma mensagem de solicitação.
        @return String
     */
     public static String leString(String msg)
     {   s = "";
         System.out.print(msg);
         try
         {
            s = d.readLine();
         }
         catch (IOException e)
         {
            System.out.println ("Erro de I/O: " + e);
         }
         return (s);
     }
    
     /**
        Lê um caractere exibindo na tela uma mensagem de solicitação.
        @return Char
     */
     public static Character leChar(String msg)
     {   s = "";
         System.out.print(msg);
         try
         {
            s = d.readLine();
         }
         catch (IOException e)
         {
            System.out.println ("Erro de I/O: " + e);
         }
         return (s.charAt(0));
     }


}//fim da classe