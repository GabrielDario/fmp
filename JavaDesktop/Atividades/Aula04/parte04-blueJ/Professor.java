public class Professor extends Usuario {
    private String areaAtuacao;

    public Professor(int mat, String nom, String log, String sen, String areaAtuacao) {
        super(mat, nom, log, sen);
        this.areaAtuacao = areaAtuacao;
    }

    public String getAreaDeAtuacao() {
        return areaAtuacao;
    }

    public void setAreaDeAtuacao(String areaAtuacao) {
        this.areaAtuacao = areaAtuacao;
    }

    @Override
    public void exibeDados() {
        System.out.println("\n--- DADOS DO PROFESSOR ---");
        super.exibeDados(); 
        System.out.println("Área de Atuação: " + areaAtuacao);
    }
}