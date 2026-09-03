

public class Aluno extends Usuario{
    private double av1;
    private double av2;
    
    public Aluno(int mat,String nom,String log,String sen) {
        super(mat,nom,log,sen);
    }
    
    public double getAv1() {
        return av1;
    }
    public double getAvv() {
        return av2;
    }
    
    public void setAv1(double nota) {
        this.av1 = nota;
    }
    public void setAv2(double nota) {
        this.av2 = nota;
    }
      public void exibeDados(){
        System.out.println("");
        System.out.println("Dados do aluno: ");
        super.exibeDados();

    }
}