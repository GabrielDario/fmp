//classe de Teste
public class CriaComputador
{
    //método main
    public static void main(String args[])
    {
        //criando o primeiro objeto: computador 1
        Computador computador1 = new Computador("Intel Celeron",1.5,520,80);

        //criando o segundo objeto: computador 2
        Computador computador2 = new Computador("Intel Pentium 4",1.5,256,40);

        //criando o terceiro objeto: computador 3
        Computador computador3 = new Computador("Intel Core Duo",1.6,2,120);

        //acessando o valor do atributo: capacidadeProcessador por meio de método de acesso do atributo
        System.out.println("Capacidade do Computador 1: " + computador1.getCapacidadeProcessador());
        System.out.println("Capacidade do Computador 2: " + computador2.getCapacidadeProcessador());
        System.out.println("Capacidade do Computador 3: " + computador3.getCapacidadeProcessador());

        //alterando o valor do atributo: capacidadeProcessador por meio de método de configuração do atributo
        computador1.setCapacidadeProcessador(2.0);

        //acessando o valor do atributo: capacidadeProcessador por meio de método de acesso do atributo
        System.out.println("Capacidade do Computador 1: " + computador1.getCapacidadeProcessador());
    }
}