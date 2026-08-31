public class TesteCofrinho {
    public static void main(String[] args) {
        Pessoa pessoa = new Pessoa("Maria");
        Cofrinho cofrinho = new Cofrinho(pessoa);

        // Deposita algumas moedas no cofrinho
        cofrinho.depositaUmaMoedaDezCentavos();
        cofrinho.depositaUmaMoedaDezCentavos();
        cofrinho.depositaUmaMoedaVinteCincoCentavos();
        cofrinho.depositaUmaMoedaCinquentaCentavos();
        cofrinho.depositaUmaMoedaCinquentaCentavos();

        // Exibe o valor total no cofrinho
        System.out.println("Total no cofrinho: R$ " + cofrinho.calculaTotal());
    }
}
