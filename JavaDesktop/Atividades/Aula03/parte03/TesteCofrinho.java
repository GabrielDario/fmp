public class TesteCofrinho {
    public static void main(String[] args) {
        String nome = Teclado.leString("Digite o nome do dono do cofrinho: ");
        Pessoa pessoa = new Pessoa(nome);
        Cofrinho cofrinho = new Cofrinho(pessoa);

        int qte10 = Teclado.leInt("Quantas moedas de 10 centavos deseja depositar? ");
        int qte25 = Teclado.leInt("Quantas moedas de 25 centavos deseja depositar? ");
        int qte50 = Teclado.leInt("Quantas moedas de 50 centavos deseja depositar? ");

        for (int i = 0; i < qte10; i++) {
            cofrinho.depositaUmaMoedaDezCentavos();
        }

        for (int i = 0; i < qte25; i++) {
            cofrinho.depositaUmaMoedaVinteCincoCentavos();
        }

        for (int i = 0; i < qte50; i++) {
            cofrinho.depositaUmaMoedaCinquentaCentavos();
        }

        // 6. Exibe os resultados na tela
        System.out.println("\n--- RESUMO DO COFRINHO ---");
        System.out.printf("Dono: %s\n", cofrinho.getDono().getNome());
        System.out.printf("Total economizado: R$ %.2f\n", cofrinho.calculaTotal());
    }
}