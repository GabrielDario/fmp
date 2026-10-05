import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        Locadora locadora = new Locadora();

        int opcao = -1;

        // WHILE mantém o sistema funcionando
        while (opcao != 0) {

            System.out.println("\n=================================");
            System.out.println("       SISTEMA DE LOCADORA");
            System.out.println("=================================");
            System.out.println("1 - Cadastrar veículo");
            System.out.println("2 - Cadastrar cliente");
            System.out.println("3 - Realizar locação");
            System.out.println("4 - Listar veículos");
            System.out.println("5 - Listar veículos disponíveis");
            System.out.println("6 - Listar veículos alugados");
            System.out.println("7 - Devolver veículo");
            System.out.println("8 - Exibir histórico");
            System.out.println("9 - Calcular multa");
            System.out.println("0 - Sair");
            System.out.print("Escolha: ");

            opcao = entrada.nextInt();
            entrada.nextLine();

            switch (opcao) {

                case 1:

                    System.out.println("\n--- CADASTRO DE VEÍCULO ---");

                    System.out.println("1 - Carro");
                    System.out.println("2 - Moto");
                    System.out.println("3 - Caminhão");

                    System.out.print("Tipo: ");
                    int tipo = entrada.nextInt();
                    entrada.nextLine();

                    System.out.print("Modelo: ");
                    String modelo = entrada.nextLine();

                    System.out.print("Marca: ");
                    String marca = entrada.nextLine();

                    System.out.print("Ano: ");
                    int ano = entrada.nextInt();
                    entrada.nextLine();

                    System.out.print("Placa: ");
                    String placa = entrada.nextLine();

                    if (tipo == 1) {

                        System.out.print("Número de portas: ");
                        int portas = entrada.nextInt();

                        Carro carro = new Carro(
                            modelo,
                            marca,
                            ano,
                            placa,
                            portas
                        );

                        locadora.cadastrarVeiculo(carro);

                    } else if (tipo == 2) {

                        System.out.print("Cilindradas: ");
                        int cilindradas = entrada.nextInt();

                        Moto moto = new Moto(
                            modelo,
                            marca,
                            ano,
                            placa,
                            cilindradas
                        );

                        locadora.cadastrarVeiculo(moto);

                    } else if (tipo == 3) {

                        System.out.print("Carga máxima em toneladas: ");
                        double carga = entrada.nextDouble();

                        Caminhao caminhao = new Caminhao(
                            modelo,
                            marca,
                            ano,
                            placa,
                            carga
                        );

                        locadora.cadastrarVeiculo(caminhao);

                    } else {

                        System.out.println("Tipo inválido!");
                    }

                    break;

                case 2:

                    System.out.println("\n--- CADASTRO DE CLIENTE ---");

                    System.out.print("Nome: ");
                    String nome = entrada.nextLine();

                    System.out.print("CPF: ");
                    String cpf = entrada.nextLine();

                    System.out.print("Idade: ");
                    int idade = entrada.nextInt();

                    Cliente cliente = new Cliente(nome, cpf, idade);

                    locadora.cadastrarCliente(cliente);

                    break;

                case 3:

                    System.out.println("\n--- REALIZAR LOCAÇÃO ---");

                    if (locadora.getQuantidadeClientes() == 0 ||
                        locadora.getQuantidadeVeiculos() == 0) {

                        System.out.println(
                            "É necessário ter cliente e veículo cadastrados."
                        );

                        break;
                    }

                    locadora.listarClientes();

                    System.out.print("Escolha o número do cliente: ");

                    int clienteIndice = entrada.nextInt();

                    Cliente clienteSelecionado =
                        locadora.getCliente(clienteIndice - 1);

                    if (clienteSelecionado == null) {
                        System.out.println("Cliente inválido!");
                        break;
                    }

                    locadora.listarVeiculosDisponiveis();

                    System.out.print("Escolha o número do veículo: ");

                    int veiculoIndice = entrada.nextInt();

                    Veiculo veiculoSelecionado =
                        locadora.getVeiculo(veiculoIndice - 1);

                    if (veiculoSelecionado == null) {
                        System.out.println("Veículo inválido!");
                        break;
                    }

                    System.out.println("1 - Contrato de 7 dias");
                    System.out.println("2 - Prazo personalizado");

                    System.out.print("Escolha: ");

                    int prazo = entrada.nextInt();

                    if (prazo == 1) {

                        // SOBRECARGA
                        locadora.realizarLocacao(
                            veiculoSelecionado,
                            clienteSelecionado
                        );

                    } else if (prazo == 2) {

                        System.out.print("Quantidade de dias: ");
                        int dias = entrada.nextInt();

                        // SOBRECARGA
                        locadora.realizarLocacao(
                            veiculoSelecionado,
                            clienteSelecionado,
                            dias
                        );

                    } else {

                        System.out.println("Opção inválida!");
                    }

                    break;

                case 4:

                    locadora.listarVeiculos();

                    break;

                case 5:

                    locadora.listarVeiculosDisponiveis();

                    break;

                case 6:

                    locadora.listarVeiculosAlugados();

                    break;

                case 7:

                    System.out.println("\n--- DEVOLUÇÃO ---");

                    locadora.listarClientes();

                    System.out.print("Número do cliente: ");

                    int clienteDev = entrada.nextInt();

                    Cliente clienteDevolucao =
                        locadora.getCliente(clienteDev - 1);

                    if (clienteDevolucao == null) {
                        System.out.println("Cliente inválido!");
                        break;
                    }

                    clienteDevolucao.listarVeiculosAlugados();

                    System.out.print("Número do veículo: ");

                    int veiculoDev = entrada.nextInt();

                    Veiculo veiculoDevolucao =
                        locadora.getVeiculo(veiculoDev - 1);

                    if (veiculoDevolucao != null) {

                        locadora.devolverVeiculo(
                            veiculoDevolucao,
                            clienteDevolucao
                        );
                    }

                    break;

                case 8:

                    locadora.exibirHistorico();

                    break;

                case 9:

                    System.out.println("\n--- CÁLCULO DE MULTA ---");

                    locadora.listarVeiculos();

                    System.out.print("Número do veículo: ");

                    int veiculoMulta = entrada.nextInt();

                    Veiculo v =
                        locadora.getVeiculo(veiculoMulta - 1);

                    if (v != null) {

                        System.out.print("Quantidade de dias de atraso: ");

                        int diasAtraso = entrada.nextInt();

                        double multa =
                            locadora.calcularMulta(
                                diasAtraso,
                                v
                            );

                        System.out.println(
                            "Valor da multa: R$ "
                            + multa
                        );
                    }

                    break;

                case 0:

                    System.out.println("Sistema encerrado.");

                    break;

                default:

                    System.out.println("Opção inválida!");
            }
        }

        entrada.close();
    }
}