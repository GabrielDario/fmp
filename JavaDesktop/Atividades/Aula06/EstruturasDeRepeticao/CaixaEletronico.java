public class CaixaEletronico {
    public static void main(String args[]) {
        ContaCorrente conta = new ContaCorrente(600.00);

        int opcao;

        do {
            conta.opcoes();

            opcao = Teclado.leInt("Informe a opção desejada: ");

            while (opcao < 0 || opcao > 4) {
                opcao = Teclado.leInt("Opção inválida! Informe a opção desejada: ");
            }

            double valor;
            int parcelas;

            switch (opcao) {
                case 1:
                    valor = Teclado.leDouble("Informe um valor para retirada: ");
                    conta.retirada(valor);
                    break;

                case 2: 
                    valor = Teclado.leDouble("Informe um valor para depósito: ");
                    conta.deposito(valor);
                    break;

                case 3: 
                    valor = Teclado.leDouble("Informe um valor para empréstimo: ");
                    parcelas = Teclado.leInt("Informe a qtde de parcelas: ");
                    conta.emprestimo(valor, parcelas);
                    break;

                case 4: 
                    conta.consultaSaldo();
                    break;

                default:
                    System.out.println("Encerrando o sistema!");
            }

        } while (opcao != 0); 
    }
}
