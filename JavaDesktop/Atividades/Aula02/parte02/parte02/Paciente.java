public class Paciente extends Pessoa {

    private String numeroProntuario;
    private Convenio convenio;

    public Paciente(
            String nome,
            String cpf,
            Data dataNascimento,
            String numeroProntuario,
            Convenio convenio) {

        super(nome, cpf, dataNascimento);

        this.numeroProntuario = numeroProntuario;
        this.convenio = convenio;
    }

    public void agendarConsulta(Data data) {

        System.out.println("Agendando consulta para: " + data.formatar());

        boolean autorizado =
                convenio.autorizarProcedimento("Consulta");

        if (autorizado) {
            System.out.println("Consulta autorizada!");
            System.out.println("Consulta agendada com sucesso.");
        } else {
            System.out.println("Consulta não autorizada.");
        }
    }

    @Override
    public void apresentar() {
        System.out.println("===== PACIENTE =====");
        System.out.println("Nome: " + getNome());
        System.out.println("CPF: " + getCpf());
        System.out.println(
                "Data de nascimento: "
                + getDataNascimento().formatar()
        );
        System.out.println("Prontuário: " + numeroProntuario);
        System.out.println("Convênio: " + convenio.getNome());
    }

    public String getNumeroProntuario() {
        return numeroProntuario;
    }

    public void setNumeroProntuario(String numeroProntuario) {
        this.numeroProntuario = numeroProntuario;
    }

    public Convenio getConvenio() {
        return convenio;
    }

    public void setConvenio(Convenio convenio) {
        this.convenio = convenio;
    }
}
