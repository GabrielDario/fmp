public class CriaComputador {
    public static void main(String args[]) {
        Computador computador1 = new Computador("Intel Celeron", 1.5, 520, 80);

        Computador computador2 = new Computador("Intel Pentium 4", 1.5, 256, 40);

        Computador computador3 = new Computador("Intel Core Duo", 1.6, 2, 120);

        System.out.println("Capacidade do Computador 1: " + computador1.getCapacidadeProcessador());
        System.out.println("Capacidade do Computador 2: " + computador2.getCapacidadeProcessador());
        System.out.println("Capacidade do Computador 3: " + computador3.getCapacidadeProcessador());

        computador1.setCapacidadeProcessador(2.0);

        System.out.println("Capacidade do Computador 1: " + computador1.getCapacidadeProcessador());
    }
}