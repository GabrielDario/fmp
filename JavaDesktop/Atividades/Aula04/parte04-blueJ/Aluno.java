public class Aluno extends Usuario {
    private double av1;
    private double av2;

    public Aluno(int mat, String nom, String log, String sen) {
        super(mat, nom, log, sen);
    }

    public double getAv1() {
        return av1;
    }

    public void setAv1(double nota) {
        this.av1 = nota;
    }

    public double getAv2() {
        return av2;
    }

    public void setAv2(double nota) {
        this.av2 = nota;
    }

    public double calcularMedia() {
        return (av1 + av2) / 2;
    }

    @Override
    public void exibeDados() {
        System.out.println("\n--- DADOS DO ALUNO ---");
        super.exibeDados(); 
        System.out.println("AV1: " + av1 + " | AV2: " + av2);
        System.out.println("Média: " + calcularMedia());
    }
}