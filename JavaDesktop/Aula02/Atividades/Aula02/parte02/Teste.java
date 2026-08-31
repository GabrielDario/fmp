public class Teste {

    public static void main(String[] args) {

        // Criando uma Data
        Data dataNascimento = new Data(15, 5, 1995);

        // Criando um Convênio
        Convenio convenio = new Convenio(
                "Unimed",
                "123456",
                "(48) 3333-4444"
        );

        // Criando um Paciente
        Paciente paciente = new Paciente(
                "João da Silva",
                "123.456.789-00",
                dataNascimento,
                "PRT001",
                convenio
        );

        // Apresentando os dados
        paciente.apresentar();

        System.out.println();

        // Agendando uma consulta
        Data dataConsulta = new Data(10, 9, 2026);

        paciente.agendarConsulta(dataConsulta);

        System.out.println();

        // Testando getters
        System.out.println("Nome: " + paciente.getNome());
        System.out.println("CPF: " + paciente.getCpf());
        System.out.println("Prontuário: "
                + paciente.getNumeroProntuario());

        System.out.println();

        // Testando setters
        paciente.setNome("Maria da Silva");

        System.out.println("Novo nome: "
                + paciente.getNome());
    }
}
