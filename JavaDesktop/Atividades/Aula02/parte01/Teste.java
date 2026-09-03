public class Teste {
    public static void main(String[] args) {
        System.out.println("-----COMPUTADOR-----");
        Computador pc1 = new Computador("Le novo", 2025);
        Computador pc2 = new Computador("Positivo", 1999);
        Computador pc3 = new Computador("IlhaWay", 2010);
        pc1.apresentar();
        pc2.apresentar();
        pc3.apresentar();
        System.out.println("---------------------");
        
        System.out.println("-----IMÓVEL-----:");
        Imovel imovel1 = new Imovel("Madri", 52);
        Imovel imovel2 = new Imovel("Trindade", 66);
        Imovel imovel3 = new Imovel("Kobrasol", 45);
        imovel1.apresentar();
        imovel2.apresentar();
        imovel3.apresentar();
        System.out.println("---------------------");
        
        System.out.println("-----AUTOMOVEL-----:");

        Automovel automovel1 = new Automovel("Fiat", 2019);
        Automovel automovel2 = new Automovel("Wolksvagem", 1984);
        Automovel automovel3 = new Automovel("Honda", 2001);

        automovel1.apresentar();
        automovel2.apresentar();
        automovel3.apresentar();
    }
}