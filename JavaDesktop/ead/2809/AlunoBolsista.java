public class AlunoBolsista extends Aluno {

    private String tipoBolsa;

    public AlunoBolsista(int codigo, String nome, String dataNascimento,
                         String email, String senha, String tipoBolsa) {

        super(codigo, nome, dataNascimento, email, senha);

        this.tipoBolsa = tipoBolsa;
    }

    public String getTipoBolsa() {
        return tipoBolsa;
    }

    public void setTipoBolsa(String tipoBolsa) {
        this.tipoBolsa = tipoBolsa;
    }

    @Override
    public void exibeDados() {
        super.exibeDados();
        System.out.println("Tipo de bolsa: " + tipoBolsa);
    }
}