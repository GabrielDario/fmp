public class Convenio {

    private String nome;
    private String registroAns;
    private String telefone;

    public Convenio(String nome, String registroAns, String telefone) {
        this.nome = nome;
        this.registroAns = registroAns;
        this.telefone = telefone;
    }

    public boolean autorizarProcedimento(String procedimento) {

        System.out.println("Solicitando autorização para: " + procedimento);

        // Regra simples para o exemplo
        if (procedimento.equalsIgnoreCase("Consulta")) {
            return true;
        }

        return false;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getRegistroAns() {
        return registroAns;
    }

    public void setRegistroAns(String registroAns) {
        this.registroAns = registroAns;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
}
